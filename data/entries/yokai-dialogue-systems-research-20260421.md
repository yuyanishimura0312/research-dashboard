# AIキャラクター自律会話生成システム — 研究動向調査

## 調査日: 2026-04-21
## 調査目的: 妖怪百景プロジェクトの会話バリエーション戦略構築のためのベンチマーク・ベストプラクティス確保

---

## 文献マップ

### 1. Generative Agents（生成エージェント）

**Park et al. (2023) "Generative Agents: Interactive Simulacra of Human Behavior"**
- 掲載: UIST '23 (ACM)
- 引用: 2000+
- 核心: 25体のエージェントがLLMで自律行動。記憶ストリーム→反省→計画の3層アーキテクチャ。バレンタインパーティーの自律的組織化を実証
- 妖怪SNSへの応用: 記憶→反省→計画の3層構造を妖怪の投稿生成に適用可能

### 2. マルチエージェント対話の品質

**"Cohesive Conversations: Enhancing Authenticity in Multi-Agent Simulated Dialogues" (2024)**
- 掲載: OpenReview
- 核心: SDR（Screening, Diagnosis, Regeneration）フレームワークで反復・矛盾・幻覚を検出・修正
- 妖怪SNSへの応用: 投稿生成後にSDR的チェックを入れて重複を排除

**"Who speaks next? Multi-party AI discussion leveraging turn-taking" (2025)**
- 掲載: Frontiers in AI
- 核心: マーダーミステリーゲームでの多者間AI議論。発言順序の体系化
- 妖怪SNSへの応用: 議論での発言順序を自然にするターンテイキングモデル

### 3. ペルソナ一貫性

**"Persona-Aware Alignment Framework (PAL)" (2025)**
- 掲載: Transactions of ACL / MIT Press
- 核心: ペルソナ整合性を最適化目標とし、2段階学習+Select-then-Generate推論
- 妖怪SNSへの応用: 各妖怪のペルソナカードを推論時に参照するパイプライン

**"Post Persona Alignment (PPA)" (2025)**
- 核心: まず一般的な応答を生成→ペルソナ記憶を検索→応答を一貫性のある形に修正
- 妖怪SNSへの応用: 生成→妖怪性格で修正の2段階パイプライン

**"Hello Again! LLM-powered Personalized Agent for Long-term Dialogue" (NAACL 2025)**
- 核心: 長期対話でのペルソナ維持。LD-Agentフレームワーク
- 妖怪SNSへの応用: 妖怪の過去の発言を記憶し一貫性を保つ

### 4. 感情モデル

**"Evolving Agents: Interactive Simulation of Dynamic and Diverse Human Personalities" (2024)**
- 掲載: arXiv
- 核心: 感情を0-7のスケールで数値化。感情の大きな変化が計画を変更するトリガーに
- 妖怪SNSへの応用: 妖怪の感情状態を数値管理し、投稿のトーンに反映

**"Developing conversational Virtual Humans for social emotion elicitation based on LLMs" (2024)**
- 掲載: ScienceDirect
- 核心: 性格・気分・態度の心理的構成要素をLLMと統合
- 妖怪SNSへの応用: 妖怪の気分（天気・季節・イベントで変動）を投稿に反映

### 5. 反復回避・多様性

**"A Survey on Recent Advances in LLM-based Multi-turn Dialogue Systems" (2025)**
- 掲載: ACM Computing Surveys
- 核心: マルチターン対話の品質評価：質問力、関連性、具体性、反復の4軸
- 妖怪SNSへの応用: 反復検出の4軸評価をポスト生成パイプラインに組み込む

**Trope-informed NPC dialogue design (Glasgow, 2021)**
- 核心: 会話分析の原則に基づくNPC対話設計で自然さ・知性の印象が向上
- 妖怪SNSへの応用: 妖怪のトロープ（キャラクター類型）を会話に反映

### 6. 日本語・文化特有

**"ChatHaruhi: Reviving Anime Character in Reality via LLM" (2023)**
- 掲載: arXiv
- 核心: アニメキャラの背景・性格・過去の会話を大量プロンプトに含め、キャラらしい対話を生成
- 妖怪SNSへの応用: 妖怪のlore（伝承）をプロンプトに含める手法

**"Jouzu: Interaction with Stylized Dialogue Fictional Agents" (2025)**
- 核心: アニメ風の発話スタイル（一人称、終助詞、感情的表現）を統合
- 妖怪SNSへの応用: 各妖怪の speech_style を活用した発話スタイル制御

### 7. ゲームNPC対話

**"LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms" (2025)**
- 掲載: arXiv
- 核心: Unity + Discord のクロスプラットフォームNPC対話システム
- 妖怪SNSへの応用: ゲームとSNSの両方でキャラクターが活動するモデル

---

## 研究動向サマリー

### 分野全体のトレンド

2023年のStanford Generative Agents論文を起点として、LLMベースの自律エージェント会話システムは急速に発展している。主要なトレンドは以下の5つ:

1. **記憶アーキテクチャの高度化**: 単純なコンテキストウィンドウから、記憶ストリーム→反省→計画の3層構造、さらにPost Persona Alignment（生成→検索→修正）へと進化

2. **ペルソナ一貫性の最適化**: ペルソナ整合性を単なる制約ではなく最適化目標として扱う研究が主流に。PAL（2025）やPPA（2025）が代表

3. **感情・気分モデルの統合**: 静的な性格だけでなく、動的な感情状態（怒り・喜び・悲しみ等）をリアルタイムで計算し、会話に反映する手法が成熟

4. **反復検出・回避の体系化**: SDR（Screening, Diagnosis, Regeneration）フレームワークのように、生成後に品質チェックを入れるパイプラインが標準に

5. **文化特有の対話スタイル**: 日本語の役割語（キャラクター語）、アニメトロープ、敬語体系などをLLMに統合する研究が活発

### 論争点・未解決の問い

- **スケーラビリティ**: 25体のエージェント（Stanford）は成功したが、1000体以上で同等の品質を維持できるか未検証
- **長期記憶の管理**: 数ヶ月〜数年にわたるキャラクターの記憶をどう圧縮・管理するか
- **評価指標の標準化**: 「信憑性」「一貫性」「多様性」の定量評価手法が統一されていない
- **コスト**: LLM呼び出しコストと品質のトレードオフ

### 今後の研究方向

- 大規模マルチエージェント（100体以上）の社会シミュレーション
- 文化的コンテキストを深く理解するエージェント設計
- テンプレートベースとLLMベースのハイブリッドアプローチ（コスト最適化）
- ユーザーとエージェントの長期的関係構築

---

## 妖怪百景への具体的適用提案

### A. 3層記憶アーキテクチャ（Park et al.ベース）
1. **記憶ストリーム**: 過去の投稿・会話を時系列で保存
2. **反省**: 定期的に記憶を要約し、高次の洞察を生成
3. **計画**: 季節・時刻・環境データに基づき、今日の行動計画を生成

### B. SDR品質チェックパイプライン
1. **Screening**: 生成された投稿を直近50件と比較、類似度が閾値以上なら拒否
2. **Diagnosis**: 拒否された投稿の問題点を特定（反復、ペルソナ逸脱、トーン不一致）
3. **Regeneration**: 問題点を踏まえて再生成

### C. 感情状態モデル（Evolving Agentsベース）
- 各妖怪に7段階の感情スコア（怒り、喜び、悲しみ、恐怖、期待、信頼、驚き）
- 環境データ・他の妖怪の投稿・季節イベントで感情が変動
- 感情状態が投稿のトーンと話題選択に影響

### D. トピックスケジューリング
- 50カテゴリのトピックプールを管理
- 最近使ったトピックにクールダウン期間を設定
- 季節・時刻・環境データに基づくトピック重み付け

---

## Sources
- [Park et al. (2023) Generative Agents](https://arxiv.org/abs/2304.03442)
- [Cohesive Conversations: SDR Framework](https://openreview.net/forum?id=3ypWPhMGhV)
- [AutoGen: Multi-Agent Conversations](https://openreview.net/forum?id=BAakY1hNKS)
- [LLM-Driven NPCs: Cross-Platform](https://arxiv.org/html/2504.13928v1)
- [Survey on LLM Multi-turn Dialogue](https://dl.acm.org/doi/full/10.1145/3771090)
- [LD-Agent: Long-term Dialogue](https://github.com/leolee99/LD-Agent)
- [Multi-party AI Discussion Turn-taking](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1582287/full)
- [Persona-Aware Alignment (PAL)](https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.57/134310/)
- [Post Persona Alignment](https://arxiv.org/html/2506.11857)
- [Persona Consistent via Contrastive Learning](https://dl.acm.org/doi/10.1145/3543873.3587346)
- [Mem0: Scalable Long-Term Memory](https://arxiv.org/pdf/2504.19413)
- [Evolving Agents: Dynamic Personalities](https://arxiv.org/html/2404.02718v2)
- [Virtual Humans for Emotion Elicitation](https://www.sciencedirect.com/science/article/pii/S095741742400126X)
- [ChatHaruhi: Anime Character Dialogue](https://ar5iv.labs.arxiv.org/html/2308.09597)
- [Jouzu: Stylized Dialogue Agents](https://arxiv.org/html/2507.06483v1)
- [Trope-informed NPC Dialogue Design](https://eprints.gla.ac.uk/252546/2/252546.pdf)
- [Personalized Quest & Dialogue Generation](https://dl.acm.org/doi/10.1145/3544548.3581441)
- [Score Before You Speak](https://arxiv.org/html/2508.06886v1)
- [Persona-Utterance Pair Dataset](https://pmc.ncbi.nlm.nih.gov/articles/PMC12453736/)

---

## 追加調査結果（リサーチチーム2・3）

### ゲーム業界の会話設計パターン

#### The Sims: 感情トークンベースの抽象化
- 3,000〜4,000語の感情トークンで多様な雑談生成
- 「何を言うか」より「どう言うか」が重要
- **妖怪SNSへ**: 同じ話題でも感情フィルタで異なる表現を自動生成

#### Dwarf Fortress: 関係性駆動の対話
- 30回以上の会話で「長期知人関係」成立
- 性格相性で「友情」か「遺恨」が自動決定
- **妖怪SNSへ**: 関係グラフ（Attraction/Rivalry/Kinship）を構築

#### Animal Crossing: パラメータ駆動の会話分岐
- 8性格タイプ × 関係度(0-10) × 時間帯 × 天気
- 168〜300行の基本テンプレートで数万の組み合わせ
- **妖怪SNSへ**: 妖怪性格5-10種 × 関係4段階 × 季節 × 時刻

#### Stardew Valley: 段階的キャラクター開示
- 関係度0-2心: 天気の話 → 8-10心: 秘密や悩み
- **妖怪SNSへ**: 関係度で発言の「深さ」を段階変化

### 商用NPC会話システム

#### Inworld AI
- Narrative Graph（Xbox共同開発）で高次物語目標を定義
- Character Card: Personality, Knowledge, Relationships, Dialogue Style
- Barks Generator: 短い独白・環境反応を大量生成

#### Convai
- NPC-to-NPC対話: プレイヤーなしの複数エージェント会話
- マルチモーダル知覚: NPCが環境を「見る・聞く」

#### Ubisoft NEO NPC (2024)
- ライター主導の人格構築 + LLMの統計的微調整
- 認証性保持: NPCの人格が破壊されない柔軟な制約

### 反復回避の具体的手法

#### Adaptive Prompt Pruning (APP)
- 単一パラメータで多様性と一貫性のバランスを制御
- **妖怪SNSへ**: 季節進行で古い表現を段階的に削除

#### Topic Rotation System
```json
{
  "topic": "炎について",
  "last_used": "2026-04-10",
  "cooldown_days": 3
}
```
- 同じ話題のクールダウン期間を強制
- 月次（季節対応）、週次（トレンド対応）、日次（特別イベント）で更新

#### 発言プール最適サイズ
| プール規模 | 多様性 | 推奨 |
|---------|------|------|
| 10-30 | 低（繰返し多い） | MVP |
| 50-200 | 中（実用的） | **推奨** |
| 300-1000 | 高 | 大規模本番 |

### 感情モデルの詳細

#### 8感情スケール (Fallout NV方式)
怒り/嫌悪/恐怖/喜び/中立/痛み/悲しみ/驚き

#### Fixed-Persona SLMs with Modular Memory (2024-2025)
- LoRA微調整で各NPCに固有人格を付与
- 会話メモリと世界知識メモリを分離
- ランタイムスワップで複数NPC管理を軽量化

### 統合アーキテクチャ提案

```
┌─────────────────────────────────────────────┐
│  [Persona Layer]                            │
│  ├─ 固定人格パラメータ（LoRA or Card）      │
│  ├─ 動的属性（感情状態、エネルギー）       │
│  └─ 3層メモリ（エピソディック/セマンティック/関係）│
│                                             │
│  [Relationship Graph]                       │
│  ├─ 1010×1010 関係値マトリクス             │
│  ├─ 友情/遺恨/中立の自動分類              │
│  └─ クラスタリング（友人グループ自動検出） │
│                                             │
│  [Dialogue Generation]                      │
│  ├─ Topic Selection（季節×関心×関係値）    │
│  ├─ LLM Generation + Character Card制約    │
│  ├─ SDR品質チェック（反復/矛盾検出）      │
│  ├─ Semantic Diversity Filter              │
│  └─ Topic Cooldown System                  │
│                                             │
│  [Scheduling]                               │
│  ├─ 投稿タイミング（時刻/曜日/イベント）  │
│  └─ 関係構築スケジュール                   │
└─────────────────────────────────────────────┘
```

### 成果指標

| メトリクス | 現在 | 目標 |
|---------|------|------|
| 異なり語数/妖怪 | 100-200 | 500-1000 |
| 話題エントロピー | 低 | > 3.0 bits |
| 投稿繰り返し率 | 30-40% | < 10% |
| 関係値自動形成 | 手動 | 60%自動 |

### 追加Sources
- [Fixed-Persona SLMs with Modular Memory](https://arxiv.org/pdf/2511.10277)
- [Memory-Driven Role-Playing in LLMs](https://arxiv.org/html/2603.19313)
- [Exploring Diversity in LLM-Agent Conversation](https://arxiv.org/html/2412.21102v2)
- [Evolving Agents: Dynamic Personalities](https://arxiv.org/html/2404.02718v2)
- [Ubisoft NEO NPC Prototype](https://news.ubisoft.com/en-us/article/5qXdxhshJBXoanFZApdG3L/)
- [NVIDIA ACE On-Device SLM](https://www.nvidia.com/en-us/on-demand/session/gdc25-gdc1010/)
- [Inworld AI](https://inworld.ai/)
- [Convai](https://convai.com/)

---

## 追加調査: 推し妖怪エコシステム + 位置情報システム（2026-04-22）

### 位置情報システムの核心的知見

#### 座標付与の5段階精度
| レベル | 精度 | 例 | 対象妖怪数 |
|-------|------|------|---------|
| 5 | ±10m | 水木しげるロードのブロンズ像 | ~177 |
| 4 | ±100m | 特定の神社・聖地 | ~100 |
| 3 | ±10km | 市町村（遠野市等） | ~300 |
| 2 | ±100km | 地域・県単位 | ~300 |
| 1 | ±1000km | 国・大陸単位 | ~133 |

#### habitat_typeからの座標推定
- 水辺型 → 主要河川・湖沼の代表地点
- 山岳型 → 地域の最高峰・代表的山
- 森林型 → 原生林の残存地域
- 都市型 → 発祥文化圏の主要都市
- 空間型 → 展望台・山頂

#### 技術スタック推奨
- メイン地図: Mapbox GL JS（カスタマイズ性、GeoJSONネイティブ）
- 検索: Google Geocoding API
- データ形式: GeoJSON with precision_level + confidence_score

### 聖地巡礼×妖怪の経済ポテンシャル
- アニメ聖地巡礼: 訪日外国人の8.1%が訪問（299万人）
- 「君の名は。」: 岐阜県で253億円の波及効果
- 妖怪の伝承地は既に文化的コンテクストを持つ → 追加投資なしで聖地化可能

### Sources (Location Research)
- [日文研 怪異・妖怪伝承データベース](https://www.nichibun.ac.jp/YoukaiDB/)
- [水木しげるロード 全妖怪図鑑](https://mizuki.sakaiminato.net/road/)
- [遠野物語の舞台](https://tonojikan.jp/feature/towns-where-legends-are-still-told/)
- [聖地巡礼の経済効果](https://studiodot.co.jp/aurochs/20231124_319/)
- [Mapbox GL JS](https://docs.mapbox.com/mapbox-gl-js/api/)
