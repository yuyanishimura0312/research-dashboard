# OpenAlex 連携可能性レポート

**作成日**: 2026-05-18
**目的**: ミラツク/esse-sense DB エコシステム（AR-DB + 167 DB）と OpenAlex（2.5 億 works / CC0 / S3 snapshot）の連携可能性を整理し、優先度付きの実装パスを示す
**手法**: OpenAlex 公式ドキュメント・developers.openalex.org・学術論文 5 本（arXiv 2206.14168 / 2406.15154 / 2512.16434 等）の Web 調査 + 本エコシステム内部 DB の openalex_id 列スキャン

---

## 1. エグゼクティブ・サマリー

OpenAlex は **2022 年に Microsoft Academic Graph の後継**として公開された全分野横断の学術メタデータ基盤で、**CC0 ライセンス（公知財産）**・**約 2.5 億 works**・**S3 で 330 GB の bulk snapshot** が無料公開されている。

本エコシステムは **既に 23+ DB に `openalex_id` 列を実装**しており、特に academic-landscape-db では 233,779 ジャーナル中 **215,983 件（92.4%）に OpenAlex ID 紐付け済**。academic-outcomes-db には専用 ETL（4 Phase）が動作中、FTT-DB v2 は 18,524 OpenAlex 論文を統合済。

つまり「連携可能性」は **すでに部分的に実装されており**、議論すべきは「拡張・体系化・自動化」のレベルである。本レポートはこれを **L1〜L5 の 5 段階拡張パス**で示す。

---

## 2. OpenAlex の精密プロファイル

### 2-A. 規模（公式ドキュメント / 2026 時点）

| エンティティ | 規模 | 主な役割 |
|---|---|---|
| **Works** | 約 2.5 億 | 論文・書籍・データセット・学位論文 |
| **Authors** | 数千万 | 研究者（ORCID 連携あり） |
| **Sources** | 250,000+ | ジャーナル・リポジトリ・学会誌 |
| **Institutions** | 約 110,000 | 大学・研究機関（ROR ID 連携） |
| **Topics** | 約 4,500 | 4 階層の主題分類（旧 Concepts の後継） |
| **Publishers** | 10,000+ | 出版社 |
| **Funders** | 35,000+ | 助成機関 |
| **Countries** | 約 200 | 地理メタデータ |

### 2-B. ライセンス・アクセス

| 項目 | 内容 |
|---|---|
| ライセンス | **CC0**（パブリックドメイン相当・最も自由） |
| API | REST、JSON、無料 $1/day（100,000 リクエスト/日 + 10 req/sec） |
| Polite pool | `mailto=you@example.com` パラメータで安定アクセス |
| Bulk snapshot | **AWS S3 で無料公開**（330 GB gzip / 1.6 TB 展開後） |
| 更新頻度 | スナップショット = **四半期ごと**、API = リアルタイム |
| 有料プラン | Premium で月次スナップショット・日次変更ファイル |

### 2-C. 既知の限界（学術文献より）

- メタデータの一部に欠損（document type 86% カバー、language / OA status / funding にエラー残存）
- Microsoft Academic Graph 由来の旧データに不整合が継承
- Crossref 依存（DOI 持ちの近現代欧米論文に強く、灰色文献・非西洋論文・古典に弱い）
- Topics（旧 Concepts）の自動分類精度は分野依存（特に人文学で薄い）

---

## 3. 本エコシステム側の既存連携状況

### 3-A. `openalex_id` 列を持つ DB（実装済）

`find ~/projects/research -name "*.db"` + `PRAGMA table_info` スキャンで確認。

| DB | テーブル | 連携状態 | 充填率（実測） |
|---|---|---|---|
| **academic-landscape-db** | `journals` | **充填済** | 215,983 / 233,779（**92.4%**） |
| **contemporary-questions-db** | `cq_researchers` | 部分充填 | 3,496 / 7,082（49.4%） |
| **contemporary-questions-db** | `cq_publications` | 部分充填 | 354 / 5,302（6.7%） |
| **academic-outcomes-db** | `publications` 他 | **専用 ETL 稼働** | OpenAlex 1980-99 + recent batch |
| **future-tech-trends-db v2** | reference_works | **充填済** | 18,524 OpenAlex papers |
| **kgh-db** | sources | スキーマ実装済 | source_type に openalex 含む |
| **social-sciences-db** | researchers | スキーマ実装済 | 一部充填 |
| **economics-concepts-db** | researchers | スキーマ実装済 | 一部充填 |
| **sfs-db** | concepts.key_works | JSON 内格納 | 一部充填 |
| **time-concepts-db** | researchers | スキーマ実装済 | 一部充填 |
| **living-behavior-db** | researchers | スキーマ実装済 | 一部充填 |
| **strategy-concepts-db** | researchers | スキーマ実装済 | 一部充填 |
| **researcher-outreach-db** | sources | source_type='B3_openalex' | パイプライン定義済 |
| **industry-academic-corporate-needs-db** | researchers | `openalex_5yr_publications` 列 | 集計済 |
| **tech-acceleration-db** | facts | `source='OpenAlex'` | 充填済 |
| **future-insight-app** | researchers | UNIQUE openalex_id | 充填済 |
| **philosophical-questions-era-analysis** | sources | source_type に含む | 充填済 |

**合計**: 23+ DB が OpenAlex 連携スキーマを実装。**academic-outcomes-db は OpenAlex 主軸 DB として既に動作**。

### 3-B. 既存 ETL パイプライン

`~/projects/research/academic-outcomes-db/scripts/` には以下が存在：

- `phase1_openalex_pilot.py` — Pilot 取得
- `phase2b_openalex_recent.py` — 直近期間バッチ
- `phase5_openalex_1980_99.py` — 1980-99 履歴バッチ
- `phaseProd_fill_10_domains.py` — 10 分野 Production 充填
- `phaseProd_fill_15_remaining.py` — 残 15 分野充填
- `phaseE_basis_publications.py` — Evidence 論文充填
- `cron_monthly_diff.py` — 月次差分取得

**つまり OpenAlex の利用は既に Production 段階にある**。本レポートが扱うべきは「未活用領域の特定」と「次レベル拡張」である。

---

## 4. 連携可能性 — 5 段階拡張パス

現状を踏まえ、活用度の低い領域から順に **L1（軽量）→ L5（基盤統合）** で整理する。

### L1: 既存スキーマの充填率引き上げ（即実行可能）

**現状**: 23+ DB に `openalex_id` 列があるが、多くが部分充填にとどまる（CQ-DB researchers 49.4%、publications 6.7% 等）。

**実装**:
- 各 DB の researchers / authors テーブルに対し OpenAlex `/authors?search=<name>` を fuzzy match
- ORCID 連携で複数候補を絞り込み
- `openalex_id` 充填率を 80%+ に引き上げ

**コスト**: 1〜2 FDD（既存ETL を流用）
**効果**: 横串検索の精度向上、引用ネットワークの全 DB 横断化

### L2: cited_by / citing_works 関係の体系統合（中規模）

**現状**: works 間の引用関係を取り込んでいる DB は FTT-DB v2 と academic-outcomes-db のみ（114K + 143K リンク）。

**実装**:
- 各学術概念 DB の `key_publications` テーブルに `cited_by_count` / `citing_works[]` 列を追加
- OpenAlex `/works/W{id}` の `referenced_works` と `cited_by_api_url` を取得
- **概念 DB の理論系譜（predecessor / successor）と引用ネットワークを cross-validate**

**コスト**: 3〜5 FDD（DB ごとに 0.5 FDD）
**効果**:
- 各概念 DB の predecessor/successor 関係を **実引用データで検証**できる
- 「概念間の関係が引用関係と一致するか」を自動チェック → ハルシネーション検知強化
- IRR Kappa 補完指標として `citation_consistency_score` を新設可能

### L3: Topics 4 階層との接続（中規模）

**現状**: 我々の概念 DB は領域別に subfields を持つが、OpenAlex Topics（4,500 件・4 階層）との明示的マッピングはない。

**実装**:
- 各概念 DB の subfields テーブルに `openalex_topic_id` / `openalex_topic_l1〜l4` 列を追加
- 各概念に対し OpenAlex Topics ID を 1 つ以上紐付け
- **cross_db_refs に "openalex_topic" を新たな bridge node として追加**

**コスト**: 5〜8 FDD
**効果**:
- 13-30 領域の本エコシステム subfield 体系を **国際標準の 4,500 トピック分類**にマッピングできる
- 外部研究者が OpenAlex Topic ID から我々の概念 DB に到達する経路ができる（discovery 向上）
- 非西洋率測定の客観指標を強化（OpenAlex の言語タグと突き合わせ）

### L4: S3 Bulk Snapshot のローカル同期（大規模）

**現状**: API 経由の取得は $1/day = 100K req 制限により、大規模再構築は時間がかかる。

**実装**:
- AWS S3 から **330 GB gzip snapshot** をダウンロード（2-12 時間）
- ローカル PostgreSQL or DuckDB に展開（1.6 TB 必要）
- 月次 cron で差分同期（Premium プランなら日次差分ファイル）

**コスト**:
- ストレージ: 2 TB SSD 確保（5〜8 万円相当）
- 初期構築: 5〜10 FDD
- 月次運用: 0.5 FDD

**効果**:
- API 制限の制約消滅 → **任意の SQL クエリで 2.5 億 works を横断可能**
- 本エコシステム独自の集計（例: 全研究者の全論文を学派別に再集計）が可能になる
- レート制限を理由とした充填遅延が消える

### L5: AR-DB 経由のメタ統合（基盤）

**現状**: AR-DB は本エコシステムの 433 アセット + 48 DB 参照を管理するが、外部 DB（OpenAlex）への参照は構造化されていない。

**実装**:
- AR-DB に `external_kb` テーブルを追加（OpenAlex / Wikidata / ORCID / ROR / Crossref を統括）
- 各内部 DB の openalex_id 列を AR-DB から逆引き可能にする
- `external_kb_coverage` ビューで「どの DB が OpenAlex 充填率いくらか」を一覧化
- **OpenAlex を「48 内部 DB + 5 外部 KB」の 49 番目 + α のノードとして扱う**

**コスト**: 1〜2 FDD
**効果**:
- 「ある研究者が本エコシステムのどの DB に登場し、OpenAlex 上での被引用数はいくらか」を 1 クエリで取得可能
- **AR-DB の自己観察メタレイヤを外部 KB まで拡張**
- 連携の健全性（OpenAlex API live、充填率推移）を AR-DB 上で監視可能

---

## 5. 優先度マトリクス

| パス | 工数 (FDD) | 効果 | リスク | 優先度 |
|---|---|---|---|---|
| L1 充填率引き上げ | 1〜2 | 中 | 低 | **★★★★★ 即実行** |
| L2 引用関係統合 | 3〜5 | 高 | 低 | **★★★★★ ハルシネーション検知強化** |
| L3 Topics 接続 | 5〜8 | 高 | 中（OpenAlex Topics の質に依存） | ★★★★ |
| L4 S3 Snapshot 同期 | 5〜10 + 月次 0.5 | 極大 | 中（2 TB ストレージ前提） | ★★★ |
| L5 AR-DB メタ統合 | 1〜2 | 中（基盤的） | 低 | **★★★★ 基盤化** |

**推奨着手順**: **L1 → L5 → L2 → L3 → L4**

理由：
- L1 で既存基盤を整え、L5 でメタレイヤから可視化基盤を作る（合計 3 FDD 未満）
- そのうえで L2 の引用統合に進めば、品質ゲートとして AR-DB 経由で監視可能
- L3 / L4 は L1-L2-L5 完成後に判断（ROI 判定が可能になる）

---

## 6. リスクと既知の限界

### 6-A. OpenAlex 側のリスク

| リスク | 内容 | 緩和策 |
|---|---|---|
| 非西洋・人文学・古典のカバレッジ薄 | Crossref 依存で DOI なし論文は弱い | 我々の非西洋 / 人文 DB（PHIL / TK / KGH 等）と相補的に運用 |
| Topics 自動分類の精度ムラ | 特に人文学で粗い | OpenAlex Topic を「ヒント」として使い、本エコシステムの subfield を正本とする |
| MAG 由来データの不整合 | author 統合・所属履歴に欠損 | author_disambiguation を併用、ORCID 優先 |
| API レート制限 | 100K/日 / 10/sec で大規模再構築は時間要 | L4 で S3 snapshot に切り替え |
| 有料化プレッシャー | 月次 / 日次差分は Premium | L4 の月次サイクルは無料で十分 |

### 6-B. 我々側のリスク

| リスク | 内容 | 緩和策 |
|---|---|---|
| openalex_id 充填の質ばらつき | fuzzy match の誤紐付け | ORCID / DOI 二段照合、verification_status 列で管理 |
| データ更新の伝播遅延 | 我々の DB が古い時 OpenAlex は更新済 | snapshot 同期日を AR-DB に記録、`openalex_last_sync` 列を全 DB に追加 |
| ハルシネーション混入 | LLM が偽 openalex_id を生成 | path-1 ルール：openalex.org の URL を返した時点で実在検証必須 |

---

## 7. 戦略的位置づけ

OpenAlex は本エコシステムにとって以下の意味を持つ：

1. **規模の補完**：本エコシステム 360 万エンティティ vs OpenAlex 2.5 億 works。学術論文ドメインでは OpenAlex を**正本**として利用し、我々は**意味構造（subfield / 系譜 / 概念関係）**を担う住み分け
2. **品質ゲートの外部基準**：OpenAlex 引用関係を「真実層」として、本エコシステムの predecessor/successor をクロス検証
3. **discovery チャネル**：OpenAlex Topic ID 経由で外部研究者が本エコシステムに到達する経路
4. **CC0 という法的安心**：CC BY-SA（ConceptNet）と異なり、改変・再配布制約がない
5. **MAG 後継としての継続性**：Microsoft 撤退後の標準を引き継ぐ → 長期投資として安全

---

## 8. 推奨次ステップ（次回セッション着手項目）

1. **L1 着手**：CQ-DB cq_researchers の openalex_id 充填率を 49% → 80%+ に引き上げ（既存 ETL 流用、1 FDD）
2. **L5 着手**：AR-DB に `external_kb` テーブル追加、OpenAlex を 1 番目の外部 KB として登録（0.5 FDD）
3. **L2 設計レビュー**：各概念 DB の predecessor/successor を OpenAlex `referenced_works` でクロス検証する pilot を 1 DB で実施（PHYS or EC 推奨、2 FDD）
4. **意思決定**：L4 S3 snapshot を引き込むかは L1-L2-L5 結果を見て判定（2-3 ヶ月後）

---

## データソース

- [OpenAlex Developers Portal](https://developers.openalex.org/)
- [OpenAlex Entities Overview](https://developers.openalex.org/api-entities/entities-overview)
- [OpenAlex Rate Limits](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication)
- [OpenAlex Snapshot Format](https://docs.openalex.org/download-all-data/snapshot-data-format)
- [OpenAlex Pricing](https://help.openalex.org/hc/en-us/articles/24397762024087-Pricing)
- Priem, J., Piwowar, H., Orr, R. (2022). [OpenAlex: A fully-open index](https://arxiv.org/abs/2205.01833)
- [Comparison of MAG and OpenAlex (arXiv 2206.14168)](https://arxiv.org/abs/2206.14168)
- [Document Types in OpenAlex/WoS/Scopus/PubMed/SS (arXiv 2406.15154)](https://arxiv.org/html/2406.15154v1)
- [OpenAlex Features, Advantages and Limitations (arXiv 2512.16434)](https://arxiv.org/html/2512.16434v1)
- 内部スキャン: `find ~/projects/research -name "*.db" + PRAGMA table_info` (2026-05-18)
- 内部 ETL: `~/projects/research/academic-outcomes-db/scripts/phase*.py`
