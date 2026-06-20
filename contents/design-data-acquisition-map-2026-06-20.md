# デザインデータ取得マップ — Web/モバイル/スライド設計のトップレベル追随

**作成**: 2026-06-20 / **目的**: ミラツク・esse-sense が Web アプリ・スマホアプリ・スライドのデザインで世界トップレベルに追いつくため、世界中から「取得すべきデータ・データソース・参照体系」を発見し、既存資産と突合して取得計画に落とす。

**体制**: 5レーン並列リサーチ（R1 Web / R2 モバイル / R3 スライド / R4 横断基盤 / R5 既存資産突合）を編成し、計約90件のデータ源を発見・優先度付けした。

---

## 1. 全体の所見（地の文）

調査の結論を一言でいえば、ミラツクの設計知は**概念のレベルでは世界水準に近い**ところまで到達している一方で、**実装の実値が空いている**。デザイン学（DSD 5,793概念）、アプリ成長UX（AAG 3,108）、一枚画像美学（PIC 1,433）、編集デザイン規格（EDD）、そして統合スパインの DSK-DB が 161→395件へ成長し「空白補完の現用エンジン」として機能している。

しかし、(1) データ可視化の設計体系、(2) デザインシステムの実トークンJSON階調、(3) モバイルネイティブの実規範値、(4) アクセシビリティの実装値、という4つの実装層に明確な空白がある。これらはいずれも公開（open）で取得可能であり、Web・モバイル・スライドの全領域に効く。

さらに構造的に重要な発見として、**データ源アトラス（取得先の正本台帳）にデザイン領域が完全に不在**だった（sources 47件にdesign/font/UX系ゼロ、applied domain にもdesign/web/uxなし、non_adopted にもデザイン系なし）。アトラスが空白のまま取得を始めると重複取得・出所不明データの混入を防げないため、取得に先立ってデザインソースをアトラスへ additive 登録する必要がある（本マップ作成と同時に実施）。

---

## 2. 第1陣で取りに行くべきデータ（横断統合・重複排除）

| # | 取得対象 | 効く領域 | 取得方法 | 経路 |
|---|---|---|---|---|
| 1 | データ可視化の設計体系（Tufte/Cleveland/Munzner/Few ＋ D3/Observable 実装） | Web・スライド・DBダッシュボード | open（学術=OpenAlex / 実装=公開） | [A] 概念DB |
| 2 | デザインシステム実トークンJSON（Material 3 / Radix / shadcn / Polaris / Fluent） | Web・モバイル | open（CC-BY/MIT・GitHub直取得） | [B]実DB＋[C]DSK深化 |
| 3 | W3C デザイントークン標準 2025.10 ＋ Style Dictionary | 全領域（相互運用の土台） | open（W3C/Apache） | [C] DSK/tokens.css 連携 |
| 4 | モバイル実規範（Apple HIG＋SF Symbols / Material 3 Expressive Figmaキット） | モバイル | open（公式・無料DL） | [B] 実DB |
| 5 | アクセシビリティ実装値（WCAG 2.2 達成基準・ARIA APG・axe-core・WebAIM Million） | 全領域 | open（W3C/MPL・完全無料） | [B] 実DB |
| 6 | モバイルUI事例コーパス（Mobbin / Page Flows） | モバイル | 有料・再配布不可（参照のみ） | 参照運用（DB化しない） |
| 7 | スライド正典＋実測（Duarte Resonate無料版 / Minto SCQA / Tufte / DocSend / BCGデッキ / think-cell） | スライド | 多くopen（一部paywall） | [A]概念＋ベンチ採取 |
| 8 | 色科学 OKLCH ＋ Noto CJK/Google Fonts API | 全領域（既存tokens.css直結） | open | [C] DSK深化 |
| 9 | アジア圏モバイル（Alipay+ UXG / WeChat WeUI / Toss SLASH） | モバイル | open（公式） | [B] 実DB |
| 10 | ベンチ採取の拡張＋失敗5件の再採取（Awwwards受賞→extract.sh／britishmuseum等403/SPA） | Web・スライド | open（CSS観察） | 既存ツール extract.sh |

---

## 3. レーン別 主要ソース（URL/ライセンス/優先度）

### R1 Web アプリ設計
- W3C デザイントークン標準 DTCG 2025.10 — https://www.designtokens.org/tr/drafts/format/ — W3C-CLA / open / 高
- Material Design 3 tokens — https://github.com/material-foundation/material-tokens — Apache-2.0 / open / 高
- Style Dictionary v5 — https://github.com/style-dictionary/style-dictionary — Apache-2.0 / open / 高
- IBM Carbon — https://github.com/carbon-design-system/carbon — Apache-2.0 / 中
- Shopify Polaris tokens — https://github.com/Shopify/polaris-tokens — MIT / 中
- Microsoft Fluent 2 tokens — https://github.com/microsoft/fluentui-token-pipeline — MIT / 中
- GOV.UK Frontend — https://github.com/alphagov/govuk-frontend — MIT+OGL / 中
- Adobe Spectrum design data — https://github.com/adobe/spectrum-design-data — Apache-2.0 / 中
- GitHub Primer — https://primer.style/ — MIT / 中
- Ant Design 5（アジア最大）— https://github.com/ant-design/ant-design — MIT / 中
- shadcn/ui + Radix Primitives — https://ui.shadcn.com / https://github.com/radix-ui/primitives — MIT / 中
- Awwwards / Godly / CSS Design Awards（受賞アーカイブ=採取起点）— https://www.awwwards.com/websites/ — 各サイト著作権・bulk禁止 / 高（URL採取目的）
- 実サイトCSS採取（ベンチ拡張）— ~/tools/design-benchmark/extract.sh — CSS観察 / 高
- Observable + D3 ギャラリー — https://observablehq.com / https://d3js.org — BSD-3 / 高
- easings.net — https://easings.net/ — MIT / 高
- Motion One — https://motion.dev/ — MIT / 中

### R2 スマホアプリ設計
- Apple HIG + SF Symbols 7（iOS 26 Liquid Glass）— https://developer.apple.com/design/human-interface-guidelines/ — 利用規約 / open / 高
- Material Design 3 Expressive Figmaキット — https://m3.material.io/ — Apache-2.0 / open / 高
- WeChat WeUI（中国スーパーアプリ）— https://weui.io/ — MIT / open / 高
- Mobbin（40万スクリーン）— https://mobbin.com/ — 有料・再配布不可 / 高（参照）
- Page Flows（ユーザーフロー録画）— https://pageflows.com/ — paywall / 高（参照）
- Scrnshts（App Storeスクショ）— https://scrnshts.club/ — open / 中
- GameAnalytics ベンチ（D1/D7/D28）— https://www.gameanalytics.com/reports/ — open PDF / 高
- UXCam UX Benchmark（業種別retention）— https://uxcam.com/blog/mobile-app-retention-benchmarks/ — open / 高
- Sensor Tower 公開レポート — https://sensortower.com/ — open（詳細は有料）/ 中
- Steven Hoober サムゾーン研究 — Smashing Magazine — open / 高
- NN/g タッチターゲット — https://www.nngroup.com/articles/touch-target-size/ — open / 中
- LottieFiles / Lottie 仕様 — https://lottiefiles.com/ — open（個別ライセンス混在）/ 中
- WCAG 2.2 モバイル要件 — https://www.w3.org/TR/WCAG22/ — W3C / open / 中
- Alipay+ UX Guidelines — https://docs.alipayplus.com/ — open / 高
- Toss SLASH（韓国フィンテックUX）— https://github.com/toss/slash-site — open / 高
- LINE LIFF / engineering blog — https://developers.line.biz/ — open / 中
- Huawei ArkUI / HarmonyOS Design — https://developer.huawei.com/consumer/en/design/ — open / 低

### R3 スライド設計
- Duarte Resonate（無料電子書籍・Sparkline）— https://www.duarte.com/resources/guides-tools/resonate-ebook/ — open / 高
- Minto Pyramid Principle / SCQA — https://managementconsulted.com/scqa-framework/ — 一部open / 高
- 実BCGデッキ集（Slideworks 105件）+ think-cell テンプレ — https://slideworks.io/ / https://www.think-cell.com/en/think-cell-slide-templates — 参照/登録 / 高
- Tufte「The Cognitive Style of PowerPoint」（反面教師）— https://archive.org/details/cognitivestyleof0000tuft — open(IA) / 高
- DocSend ピッチデック実測 — https://www.dropbox.com/resources/docsend-pitch-deck-research — 登録open / 高
- Sequoia ピッチデックテンプレ — https://www.slideshare.net/slideshow/sequoia-capital-pitchdecktemplate/46231251 — open / 高
- CB Insights ユニコーン29社デック — https://www.cbinsights.com/research/billion-dollar-startup-pitch-decks/ — トライアル / 高
- Storytelling with Data（チャート選択）— https://www.storytellingwithdata.com/books — 書籍 / 高
- Presentation Zen — https://www.presentationzen.com/ — 一部open / 中
- Gamma デザインガイド（AIスライド設計知）— https://gamma.app/ — open / 中
- SpeakerDeck（デッキコーパス）— https://speakerdeck.com/ — open / 中
- SlideShare1M（Stanford 100万枚データセット）— https://exhibits.stanford.edu/data/catalog/mv327tb8364 — 要確認 / 中（DB化価値高）
- 高橋メソッド/もんたメソッド（日本発）— http://www.rubycolor.org/takahashi/ — 公知 / 中
- Marp/Slidev/reveal.js テーマ — https://sli.dev/ — MIT / 中
- Mayer/Sweller マルチメディア学習・認知負荷（OpenAlex経由）— 学術 / 低
- 日本コンサルスライド書籍群 — paywall / 低

### R4 横断基盤
- Google Fonts Developer API + Axis Registry — https://developers.google.com/fonts/docs/developer_api — free_with_key / 高
- notofonts/noto-cjk（Noto Sans/Serif CJK）— https://github.com/notofonts/noto-cjk — OFL-1.1 / 高
- HTTP Archive Web Almanac 2025 フォント章 — https://almanac.httparchive.org/en/2025/fonts — CC-BY-4.0 / 高
- OKLCH 実装ガイド + MDN — https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl — open / 高
- ColorBrewer 2.0（色覚多様性）— https://github.com/axismaps/colorbrewer — Apache-2.0 / 中
- APCA（知覚コントラスト・WCAG3流動的）— https://github.com/Myndex/apca-w3 — 要確認 / 中
- Material 3 motion tokens — https://m3.material.io/styles/motion/ — Apache-2.0 / 中
- Robert Penner easing — https://robertpenner.com/easing/ — open / 低
- WebAIM Million 2026 — https://webaim.org/projects/million/ — open / 高
- ARIA Authoring Practices Guide — https://www.w3.org/WAI/ARIA/apg/ — W3C / 高
- axe-core — https://github.com/dequelabs/axe-core — MPL-2.0 / 高
- WCAG 2.2 / JIS X 8341-3 / EAA — https://www.w3.org/WAI/standards-guidelines/wcag/ — open（JIS原文有料）/ 中
- OpenAlex API（HCI論文 主経路 / arXiv直叩き禁止の代替）— https://openalex.org — CC0 / 高
- 処理流暢性×美的ユーザビリティ効果 論文群（OpenAlex取得）— 学術 / 中
- HTTP Archive / BigQuery / CrUX — https://httparchive.org/reports — CC0 / 中
- W3C DTCG 2025.10 — https://www.designtokens.org/tr/drafts/format/ — W3C-CLA / 中
- Tokens Studio（Figma↔GitHub同期）— https://docs.tokens.studio/ — MIT相当 / 中
- Style Dictionary — https://styledictionary.com — Apache-2.0 / 中
- 源ノ角ゴシック（Source Han Sans）— https://github.com/adobe-fonts/source-han-sans — OFL-1.1 / 低
- モリサワ TypeSquare — https://typesquare.com/ — paywall / 低

---

## 4. gap マップ（既存資産との突合 / R5）

| 軸 | カバー済（取りに行かない） | 部分（深化で足りる） | 空白（取りに行く） |
|---|---|---|---|
| Web | DSD 5,793 / AAG visual・ux 389 / ベンチ~10サイト / DSDB 850 / EDD copy 1,191 / DSK 395 | DSDB実測トークン薄（typography_specs 27）/ ベンチ採取失敗5件 | デザインシステム実トークンJSON / Webコンポーネント実装体系 / モーション実カーブ |
| モバイル | AAG mobile_specific_ux 147（概念） | DSDB の AS site_type はWeb中心 | HIG/Material 実数値 / アプリ画面実採取 / ジェスチャ・触覚 |
| スライド | PIC 1,433 / EDD layout_canons 30・grid 40・trim 30 / html-slide規格 | スライド情報構造のDB化が未 | プレゼン実ベンチ採取 / データ可視化設計 / 図解パターン体系 |
| 横断 | — | DSK が処理流暢性/間/侘/幽玄を補完中（OpenAlex接地は未） | アクセシビリティ実装値 / dominant-color LQIP 等の高級実装 |

**既存設計DB インベントリ（実COUNT 2026-06-20）**: DSD 5,793 / EDD（copy 1,191・fonts 764・theory 446・works 2,893 等）/ DSDB（sites 850・typography_specs 27）/ AAG 3,108 / PIC 1,433 / DSK 395 / ベンチ採取 ~10サイト成功。MDD は実体不在（0バイト）。

---

## 5. 取得計画（経路と順序）

経路: [A] /adb 概念DB構築 / [B] /db-blindspot→/db-build 実データDB / [C] /ddb 既存DB(DSK)深化。

0. **前提整備（最優先・additive）**: デザインソースをデータ源アトラスへ登録（applied domain `design_ux` 新設）、ACM Digital Library を Web/モバイルUX分野の権威源に昇格（field_specific=1）。← 本マップと同時に実施。
1. **データ可視化設計DB**（最大の空白・全領域に効く）= [A] /adb。学術（Tufte/Cleveland/Munzner/Few・OpenAlex経由）＋実装（D3/Observable）。
2. **デザインシステム実トークンJSON**（Material3/Radix/shadcn/Polaris/Fluent）= [B] 実DB＋DSK [C] 深化。GitHub公開JSONを取得。
3. **モバイル実規範値**（HIG/Material 実数値＋アジア圏 Alipay+/WeUI/Toss）= [B]。
4. **アクセシビリティ実装値**（WCAG 2.2 達成基準・ARIA APG・axe-core）= [B]。axe-core は safe-deploy へCI統合も。
5. **スライド情報構造のDB化＋実ベンチ採取**（pitch/keynote/Duarte/Minto）= [C]＋extract.sh。失敗5サイト再採取も同時。

取得物は最終的に DSK-DB と Claude Design（claude.ai/design）のカードへ流し込み、見本帳の根拠を厚くする。

---

## 6. ライセンス・運用上の注意

- 受賞アーカイブ（Awwwards/Godly/CSS Design Awards）・UI事例（Mobbin/Page Flows）は**再配布不可・bulk scrape禁止**。利用は「採取起点URLの収集」「参照」に限定。
- 学術（ACM/IEEE/論文）は **arXiv直叩き禁止 → OpenAlex 経由**でメタデータ取得（既存鉄則準拠）。
- APCA/WCAG 3.0 は流動的で「今は実装基準にしない」。WCAG 2.2 を一次基準、APCA は補助的知覚検証に留める。
- JIS X 8341-3 原文は有料（経産省要約は無料・規範引用には不適）。Figma Variables API は Enterprise 限定。
- 全取得は additive。既存資産（DSD/EDD/DSDB/AAG/PIC/DSK）を壊さない。

---

*作成: Claude Code（5レーン並列リサーチ R1-R5 の統合）。一次データは各レーンの構造化出力に保持。*
