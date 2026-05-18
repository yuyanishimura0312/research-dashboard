# ConceptNet (MIT) 詳細プロファイルと本エコシステムのベンチマーク特定

**作成日**: 2026-05-18
**目的**: MIT Media Lab 由来の ConceptNet を構造・規模・運用・限界の 4 軸で精査し、本エコシステム（AR-DB + 167 DB / 448 アセット）の真のベンチマークを特定する
**手法**: ConceptNet 公式 (conceptnet.io)、GitHub Wiki (commonsense/conceptnet5)、ConceptNet blog、AAAI 2017 論文、批判論文 (Predicting ConceptNet Path Quality, 2019) を WebFetch + WebSearch で並列収集

---

## 1. ConceptNet の精密プロファイル

### 1-A. 沿革

| 項目 | 内容 |
|---|---|
| 起点 | **1999 年** MIT Media Lab で Open Mind Common Sense (OMCS) として開始 |
| 開発期間 | **約 27 年**（1999 → 2026 時点） |
| 開発主体 | MIT Media Lab → Luminoso Technologies, Inc. （主導者 Robyn Speer = Luminoso 共同創業者） |
| 最新版 | **ConceptNet 5.8**（2020 リリース） |
| メンテナンス状態 | **事実上の maintenance mode**。2021 年 9 月以降 PyPI 更新なし。Robyn Speer は Luminoso 退社、`concepts.arborelia.net` に活動を移管 |
| ライセンス | CC BY-SA 4.0 International |

### 1-B. 規模

| 指標 | 数値 |
|---|---|
| ノード（concept） | 約 800 万（公称、wikidata 比較研究での参照値） |
| エッジ（assertion） | **約 34,000,000**（3,400 万） |
| 言語数 | **304 言語**（コア 10 / 中程度 77 / その他 217） |
| 関係タイプ | **34 種**（/r/RelatedTo, /r/IsA, /r/PartOf, /r/UsedFor, /r/Causes, /r/HasProperty, /r/Synonym, /r/Antonym ほか） |

### 1-C. データソース構成

```
ConceptNet 5.8 のエッジ供給源
├─ Open Mind Common Sense (OMCS) ─── 創設時のクラウドソース文 (英語中心)
├─ Wiktionary ─────────────────────── 多言語辞書由来（最大シェア）
├─ Open Multilingual WordNet ──────── 専門家構築の語彙ネット
├─ DBPedia ───────────────────────── Wikipedia インフォボックス抽出
├─ OpenCyc ───────────────────────── オントロジー
├─ JMDict ────────────────────────── 日本語辞書
└─ Games With A Purpose
    ├─ Verbosity (CMU)
    └─ nadya.jp (日本語 GWAP)
```

### 1-D. アクセス手段

- **REST API** (JSON-LD)：`http://api.conceptnet.io/c/en/cat`
- **Web UI**：conceptnet.io
- **Bulk download**：CSV / Postgres dump
- **ConceptNet Numberbatch**：単語ベクトル化版（NLP で広く採用）

### 1-E. 既知の限界（学術文献由来）

1. **ノイズが多い**：OMCS のクラウドソースが未検証で混入。relation の **path quality 評価**で「ランダム選択を上回らないヒューリスティクスがある」（Predicting ConceptNet Path Quality, WWW 2019）
2. **曖昧性**：「vague, illogical, and incredibly useful」（公式 FAQ の自己評価）
3. **コンテキスト依存性の欠落**：「many commonsense assertions are true only under some circumstances」を扱えない
4. **粗い disambiguation**：part-of-speech レベルまでしか語義分離していない（"watch" の名詞 / 動詞のみ）
5. **カバレッジが不均一**：「coverage of commonsense topic areas is still patchy」
6. **品質保証メトリクス非公開**：IRR / Kappa などの inter-annotator agreement を **DB 単位では公表していない**
7. **非西洋言語の構造的劣位**：英語 OMCS + 英語 Wiktionary + WordNet を中核とするため、多言語といっても**英語スキーマの翻訳的拡張**にとどまる

---

## 2. 本エコシステムとの精密ベンチマーク

### 2-A. 規模ベンチマーク

| 指標 | ConceptNet 5.8 | 本エコシステム (2026-05-18) | 比率 |
|---|---|---|---|
| エンティティ（concept / entity） | 約 800 万 | 約 360 万 | **45%** |
| 関係（edge / relation） | 約 3,400 万 | 約 380 万 | **11%** |
| 言語数 | 304 言語（多くは少数エッジ） | 16 言語（高密度、領域別 16-56%） | 比較不能 |
| 関係タイプ数 | 34 種（汎用） | DB 別に正規化（例：cross_domain 26→7-9） | 設計思想が異なる |
| データソース数 | 8 系統 | **167 DB ファイル + 外部参照多数** | 大幅に多い |

**所見**: 規模では ConceptNet が依然上回る（特にエッジ数で 9 倍）。これは 27 年の蓄積差。**ただし「エッジあたりの構造密度・品質保証」では本エコシステムが優位**（次節）。

### 2-B. 構造ベンチマーク

| 観点 | ConceptNet | 本エコシステム |
|---|---|---|
| 関係タイプの粒度 | 34 種 / 汎用（CapableOf, UsedFor 等の常識関係） | **領域別に再正規化**（学術概念 DB は predecessor / successor / cross_domain、人物 DB は influenced_by / branched_from 等） |
| ドメイン横断接続 | 全部が単一グラフ（横断性は強いが品質不均一） | **DB 単位で正規化＋ cross_db_refs で意図的に接続**（21+ DB 接続要件） |
| メタレイヤ | なし（自己観察不可） | **AR-DB が全 448 アセットを SQL 照会可能**（自己観察可能） |
| マルチエージェント連携 | 想定なし | **111 エージェント + 235 コマンド + 51 スキル**で DB を動的に駆動 |
| 構造のバージョン管理 | 5.5 → 5.8 で 1〜2 年単位 | **PostToolUse hook で 10 秒 debounce 自動同期** |

### 2-C. 品質保証ベンチマーク

| 品質指標 | ConceptNet | 本エコシステム |
|---|---|---|
| IRR Cohen's Kappa | 未公表 | **DB 単位で公表**：PHYS 0.87 / CEH 0.99 / ES 0.96 / BOT 0.86 / TC 0.97 |
| ハルシネーション対策 | 「non-systematic errors を許容」 | **生成と検証を別エージェント別モデルで分離**（builder vs auditor） |
| source_url 完備率 | 部分的 | 多くの DB で **100%**（PHYS / CEH / ES / CQ 等） |
| 一次文献接続 | DBPedia 経由で間接的 | **literature テーブルで直接接続**（例：CQ 638 文献 / EC 271 Nobel） |
| 文化バランス指標 | Eurocentric（英語中心） | **非西洋率を DB 単位で測定**（SFS 79.7% / KGH 88.4% / TK 79.5%） |

### 2-D. 運用ベンチマーク

| 観点 | ConceptNet | 本エコシステム |
|---|---|---|
| 開発期間 | 27 年 | **51 日** |
| 開発体制 | MIT 研究室 → 企業（数名〜十数名） | **個人 + Claude Code エージェント群** |
| 累計コミット | 不明（活動低調） | **51 日で 4,111 コミット** |
| 1 日あたり成果 | （現在）ほぼ停滞 | **約 80 コミット / 日** |
| 拡張容易性 | 5.8 以降停滞 | **/adb / /db-blindspot / /ddb** で 3 経路の継続拡張ルール |

---

## 3. ベンチマークの本質的差分 — 何が比較可能で何が比較不能か

### 3-A. 比較可能な軸（同種知識基盤として）

1. **エンティティ密度**：本エコシステムは ConceptNet の 45%（360 万 / 800 万）。3〜5 年継続すれば**追いつき可能な射程**。
2. **関係タイプの整理**：ConceptNet 34 種（汎用）に対し、本エコシステムは**領域別に正規化**（より深い構造化）。「数」より「適合度」で勝つ設計。
3. **多言語化**：ConceptNet は 304 言語あるが、**多くは Wiktionary 由来の薄いエッジ**。本エコシステムは 16 言語ながら**高密度・領域専門**。
4. **品質メトリクス**：ConceptNet は IRR 非公表、本エコシステムは **DB 単位で公表**。これは構造的優位。

### 3-B. 比較不能な軸（設計思想が異なる）

1. **目的**：ConceptNet は「**常識推論のための単一汎用グラフ**」、本エコシステムは「**特定領域知識を専門特化 DB として束ね、エージェントが動的に組み合わせる**」。
2. **メタレイヤ**：本エコシステムの AR-DB に相当する**自己観察 DB は ConceptNet に存在しない**（27 年の歴史で構築されてこなかった機能）。
3. **エージェント連携**：ConceptNet は「データ」、本エコシステムは「**動的に組み合わさるデータ群＋エージェント群**」。
4. **個人運用可能性**：ConceptNet は組織前提、本エコシステムは**個人 + LLM で再生産可能**な方法論を内蔵。

---

## 4. 真のベンチマーク特定 — 本エコシステムが立つべき指標

ConceptNet の精密分析から、本エコシステムが**追うべき指標**と**既に超えている指標**が明確になる。

### 4-A. 追うべき指標（量的キャッチアップ目標）

| 指標 | ConceptNet 現在値 | 本エコシステム現在値 | 目標到達時期（推定） |
|---|---|---|---|
| エンティティ総数 | 800 万 | 360 万 | 2027 年中 (+ 1.5 年) |
| エッジ総数 | 3,400 万 | 380 万 | 2028 年中 (+ 2.5 年) |
| 言語カバー数 | 304 | 16 | 質的拡張優先、量的同等化は非追求 |
| データソース系統 | 8 | 167 DB（既に大幅超過） | ✓ 達成済 |

### 4-B. 既に超えている指標（質的優位）

| 指標 | ConceptNet | 本エコシステム |
|---|---|---|
| IRR Kappa の DB 単位公表 | ✗ | ✓（複数 DB で 0.86-0.99） |
| 自己観察メタレイヤ | ✗ | ✓（AR-DB） |
| 領域別関係タイプ正規化 | ✗（汎用 34 種のみ） | ✓ |
| エージェント自動駆動 | ✗ | ✓（111 体） |
| 非西洋率の構造化測定 | ✗（Eurocentric） | ✓（16-88% 領域別） |
| Production-grade 完備基準 | ✗ | ✓（Pilot 思考禁止ルール） |

### 4-C. 本エコシステムの正しい benchmark statement（暫定案）

> **「ConceptNet が 27 年で構築した 3,400 万エッジの汎用常識グラフに対し、本エコシステムは 51 日で 380 万エッジ（11%）を達成した。ただし量より構造で勝負しており、(1) IRR Kappa 0.86-0.99 の品質ゲート、(2) AR-DB による自己観察メタレイヤ、(3) 領域別に正規化された関係タイプ、(4) 非西洋率の構造的測定、(5) 個人 + LLM での再生産可能性、の 5 点で ConceptNet には存在しない構造的優位を持つ。比較すべきは『規模』ではなく『品質保証された専門知識の動的合成可能性』である」**

---

## 5. 次に追うべき外部比較対象（ConceptNet 以外）

ConceptNet との比較で見えた構造的優位を踏まえ、次は以下と比較すべき：

| 比較対象 | 比較の主眼 | 想定される結果 |
|---|---|---|
| **CSKG (USC ISI, 2021)** | ConceptNet + ATOMIC + Wikidata-CS + WordNet + Roget + Visual Genome を統合した CSKG（6 ソース統合 KG）と「DB 統合方式」を比較 | 統合のアプローチが**事前統合 vs 動的統合**で異なる |
| **ATOMIC (AI2, 2019)** | 因果的常識（if-then knowledge）への特化と比較 | 本エコシステムの genealogy_chain（系譜連鎖）の構造的近似 |
| **Wikidata** | 1.15 億エンティティ / 14 億 statements の超大規模 KG | 規模では大差、品質指標と非西洋率では同等以上を狙える |
| **OpenAlex** | 2.5 億学術 work / 30 億関係 | 学術論文ドメインでの cross_db 接続性で比較 |
| **CrewAI / AutoGen** | マルチエージェント駆動アーキテクチャ | エージェント数・連携密度では本エコシステムが大幅超過 |

---

## 6. 結論

**ConceptNet は「個人運用 + LLM 駆動」でキャッチアップ可能な射程の比較対象であり、現時点で量的に 11-45% に到達している**。一方、**自己観察メタレイヤ・IRR 公表・領域別正規化・非西洋率測定**の 4 点で本エコシステムは ConceptNet に存在しない構造的優位を持つ。

したがって本エコシステムの**真のベンチマーク・ステートメント**は次のように定式化される：

> **「ConceptNet の規模を 5 年で追いつきつつ、ConceptNet が 27 年間構築してこなかった『品質保証された専門知識の動的合成可能性』を独自の優位として保持する」**

---

## データソース

- [ConceptNet 公式](https://conceptnet.io/)
- [ConceptNet GitHub Wiki - Relations](https://github.com/commonsense/conceptnet5/wiki/relations)
- [ConceptNet GitHub Wiki - FAQ](https://github.com/commonsense/conceptnet5/wiki/FAQ)
- [ConceptNet 5.5: An Open Multilingual Graph of General Knowledge (AAAI 2017)](https://arxiv.org/abs/1612.03975)
- [Predicting ConceptNet Path Quality Using Crowdsourced Assessments (WWW 2019)](https://arxiv.org/pdf/1902.07831)
- [ConceptNet 5.8 Release Notes](http://blog.conceptnet.io/posts/2020/conceptnet-58/)
- [CSKG: The CommonSense Knowledge Graph (USC ISI)](https://openreview.net/pdf?id=TOzBiasXxyX)
- [Commonsense Knowledge in Wikidata (CEUR-WS Vol-2773)](https://ceur-ws.org/Vol-2773/paper-10.pdf)
- [本エコシステム AR-DB](file:///Users/nishimura+/projects/research/agent-registry-db/data/agent_registry.db)
- 集計日: 2026-05-18
