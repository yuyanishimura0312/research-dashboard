# Next.js イベント管理・学習プラットフォーム構築 ベストプラクティス調査

調査日: 2026-04-03

## 1. Next.js App Routerの設計方針

### Server Components vs Client Components

App RouterではすべてのコンポーネントがデフォルトでServer Componentとなる。イベント管理アプリでは、以下の分離が推奨される。

**Server Component（デフォルト）で実装すべきもの:**
- イベント一覧ページ（DBからのフェッチ、SEOメタデータ生成）
- イベント詳細ページ（slug動的ルートでのデータ取得）
- ダッシュボード・管理画面のレイアウト

**Client Component（"use client"宣言）にすべきもの:**
- 参加申込フォーム（useState、バリデーション）
- Stripe決済ボタン（ブラウザSDK利用）
- リアルタイム残席表示・カウントダウン
- カレンダーUI・日付フィルター

重要な原則として、`"use client"`はコンポーネントツリーのできるだけ末端（リーフ）に配置する。上位に書くとそのサブツリー全体がクライアントコンポーネントに昇格し、バンドルサイズが不必要に大きくなる。

### ルーティング構成

```
app/
  (public)/
    events/
      page.tsx              # イベント一覧（Server Component）
      [slug]/
        page.tsx            # イベント詳細（Server Component）
        opengraph-image.tsx # OGP画像生成
    layout.tsx
  (dashboard)/
    admin/
      events/
        page.tsx            # 管理画面
        [id]/edit/page.tsx
    layout.tsx
  api/
    webhooks/
      stripe/route.ts       # Stripe Webhook（Route Handler必須）
```

`generateStaticParams`を使えば、人気イベントを事前にビルド時に静的生成できる。Partial Prerendering（PPR）を活用すると、ページのシェルを静的にプリレンダリングしつつ、残席数などの動的部分をストリーミングで埋めることが可能になる。

## 2. Stripe決済統合

### Checkout Sessionフロー

2025-2026年の推奨は**Embedded Checkout**である。従来のHosted Checkoutと異なり、ユーザーを外部に遷移させずに自サイト内にiframeとして決済UIを埋め込める。実装にはServer Actionを使うのが現在の標準パターンとなっている。

```typescript
// app/actions/checkout.ts
"use server"
export async function createCheckoutSession(eventId: string) {
  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    currency: "jpy",
    line_items: [{ price: priceId, quantity: 1 }],
    payment_method_types: ["card", "konbini"],
    success_url: `${baseUrl}/events/${slug}/complete`,
    cancel_url: `${baseUrl}/events/${slug}`,
  })
  return session.url
}
```

### JPY（日本円）の注意点

JPYはゼロデシマル通貨であり、Stripeに渡す金額はそのままの整数値を使う。USD等では100を掛けてセント単位にするが、JPYでは**掛け算不要**。5000円なら`amount: 5000`とする。これを誤ると100倍の金額で決済される致命的バグになるため、通貨ごとの処理を明示的に分岐させるか、Stripe側でPrice Objectを事前作成しておくのが安全である。

### コンビニ決済（Konbini）

Konbiniは非同期決済であり、カード決済とフローが根本的に異なる。顧客がCheckoutフォームを送信しても即座に決済完了にはならず、支払い番号が発行され、コンビニでの現金支払い後に`checkout.session.completed`イベントが発火する。このため、Webhookでの非同期処理が必須となる。Konbini利用にはStripeアカウントの国設定がJapan、通貨がJPYであることが前提条件である。

### Webhook実装

Server ActionではWebhookを受けられないため、Route Handlerが必須。App Routerでは`request.text()`でraw bodyを取得する。

```typescript
// app/api/webhooks/stripe/route.ts
export async function POST(request: Request) {
  const body = await request.text()  // JSONパースしない
  const sig = request.headers.get("stripe-signature")!
  const event = stripe.webhooks.constructEvent(
    body, sig, process.env.STRIPE_WEBHOOK_SECRET!
  )
  // checkout.session.completed → 参加登録確定
  // payment_intent.payment_failed → 失敗処理
}
```

最大の落とし穴は`request.json()`を使ってしまうこと。Stripeの署名検証にはraw bodyが必要なので、必ず`request.text()`を使う。

## 3. Auth.js v5 認証設計

### プロバイダ設定

Google OAuthとメールマジックリンク（Resend経由）の併用が推奨構成。Auth.js v5ではPrismaAdapterを使ってセッションとアカウント情報をDBに永続化する。

```typescript
// auth.ts
export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: PrismaAdapter(prisma),
  providers: [
    Google({ clientId: "...", clientSecret: "..." }),
    Resend({ from: "noreply@example.com" }),  // マジックリンク
  ],
  callbacks: {
    jwt({ token, user }) {
      if (user) token.role = user.role  // DBのroleを引き継ぐ
      return token
    },
    session({ session, token }) {
      session.user.role = token.role
      return session
    },
  },
})
```

### ロールベースアクセス制御

Auth.js公式のRBACガイドに従い、Userモデルに`role`フィールド（ADMIN / ATTENDEE）を追加する。初回サインアップ時のデフォルトはATTENDEE、管理者はDB直接変更またはシード処理で設定する。

認可チェックは必ずサーバーサイドで行う。Server Component内で`const session = await auth()`を呼び、`session.user.role`を確認する。middleware.tsでルートレベルの保護も併用する。クライアント側の`useSession`はUI表示の切り替えにのみ使い、セキュリティの境界にしてはならない。

## 4. データベーススキーマ設計

Prisma + PostgreSQLを前提とした中核テーブル構成は以下の通り。

| テーブル | 主要カラム | 役割 |
|---------|-----------|------|
| User | id, email, name, role, image | 認証・ユーザー情報 |
| Event | id, slug, title, description, date, venue, capacity, price, status | イベント本体 |
| Registration | id, userId, eventId, status, stripeSessionId, paidAt | 参加登録（UserとEventの中間テーブル） |
| Ticket | id, registrationId, ticketType, qrCode | 発券情報 |
| EventSession | id, eventId, title, startTime, endTime, speakerId | 学習セッション |
| Speaker | id, name, bio, image | 登壇者情報 |

**インデックス戦略:**
- `Event.slug`にユニークインデックス（URLルーティング用）
- `Event.date`にインデックス（日付順表示、期間検索用）
- `Registration`に`(userId, eventId)`の複合ユニーク制約（重複登録防止）
- `Registration.stripeSessionId`にユニークインデックス（Webhook冪等性確保）

Registrationテーブルのstatusは `pending → confirmed → cancelled` の状態遷移を持たせる。Konbini決済では、Checkout Session作成時にpendingで登録し、Webhookで`confirmed`に更新するパターンが必須となる。

## 5. OGP画像生成（@vercel/og）

App Routerでは`next/og`からImageResponseをインポートでき、追加パッケージのインストールは不要。イベントページごとに動的OGP画像を生成するには、`opengraph-image.tsx`という規約ファイルを配置する。

```typescript
// app/(public)/events/[slug]/opengraph-image.tsx
import { ImageResponse } from "next/og"

export const size = { width: 1200, height: 630 }
export const contentType = "image/png"

export default async function OGImage({ params }: { params: { slug: string } }) {
  const event = await getEvent(params.slug)
  return new ImageResponse(
    <div style={{ display: "flex", flexDirection: "column", ... }}>
      <h1>{event.title}</h1>
      <p>{event.date} / {event.venue}</p>
    </div>,
    { ...size }
  )
}
```

**注意点:**
- デフォルトフォントはNoto Sansのみ。日本語表示には`Noto Sans JP`のフォントファイルを`fetch`で読み込んで`fonts`オプションに渡す必要がある
- ImageResponse内ではFlexboxのみ対応。CSS Gridは使えない
- 本番環境ではVercelが自動的に`Cache-Control: public, max-age=31536000`を付与する
- 画像サイズは1200x630が各SNSで最も安定して表示される

## まとめ：避けるべき落とし穴

1. **"use client"の過剰使用** -- イベント一覧や詳細のデータ表示部分までクライアントにしない
2. **JPY金額の100倍バグ** -- ゼロデシマル通貨は掛け算不要
3. **Webhook bodyのJSON parse** -- `request.text()`で取得し、`request.json()`は使わない
4. **Konbiniの同期処理前提** -- 非同期決済なのでWebhook完了まで仮登録とする
5. **クライアント側での認可判定** -- `useSession`の結果でAPIを保護しない。サーバーで検証する
6. **OGP画像の日本語フォント漏れ** -- 明示的にNoto Sans JPを読み込まないと文字化けする
