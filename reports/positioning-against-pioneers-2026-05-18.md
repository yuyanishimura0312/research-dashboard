# 先行事例の地平に立つ ── 本エコシステムの位置づけ

**作成日**: 2026-05-18
**目的**: 世界の優れた先行プロジェクトを参照点としつつ、その地平に立って本エコシステムが採った設計選択と運用上の特徴を 2,000 字で説明する
**前提**: 構造的「世界初」は主張しない。先行事例の方向性に学びつつ、運用環境に固有の翻訳として実装した立ち位置を明示する

---

知識基盤構築の世界には、本エコシステムが立っている地平を切り拓いた先行プロジェクトが複数存在する。それらを参照点としつつ、本エコシステムの設計選択と運用特徴を位置づける。

**ConceptNet（MIT Media Lab, 1999-）** は 27 年をかけて 3,400 万エッジ・304 言語の常識知識グラフを築き、領域別独立テーブル × 関係型接続というパターン C 連邦化の原型を確立した。本エコシステムも同パターンを採るが、ConceptNet が汎用 34 関係型に統一するのに対し、本エコシステムは領域別に関係型を正規化する。物理学では predecessor / successor、人物 DB では influenced_by、概念 DB では cross_domain といった具合に、領域に最適化された関係語彙を維持する。ConceptNet Numberbatch が SemEval 2017 で圧勝した到達点には届かないが、汎用と専門の中間に位置する設計を選択している。

**AWS Agent Registry（2024 preview）** は、エージェント定義のクラウド集約管理という方向性を業界に提示した先駆である。本エコシステムの AR-DB は、この方向性をローカル SQLite に翻訳した実装にあたる。クラウド API ではなく SQL 直接照会（agent_relations 1,874 件）、手動登録ではなくファイル変更からの PostToolUse hook 自動同期（9 件 / 10 秒 debounce）を選んだ。クラウド集約か、ローカル自律かという設計分岐点に立つ。

**ChatDev の CEO オーケストレーター層、AgentOrchestra（arXiv 2506.12508）の階層構造** は、メタオーケストレーションを多層化する研究の先駆だった。本エコシステムはこれを Tier -1〜3 の 5 層（meta 34 / orchestrator 27 / team 26 / specialist 110 / utility 251）に展開し、型自動判定（/db-master が概念 DB / 実データ DB / 既存深化を見分けてルーティング）を統合した。

**OpenAlex（2022 MAG 後継）** は、Crossref・ORCID・ROR を統合した 2.5 億 works の学術メタデータを CC0 で公開する基盤として、学術知識のインフラ層を担う。本エコシステムは 23+ DB に `openalex_id` 列を実装し、academic-landscape-db では 233,779 ジャーナル中 215,983 件（92.4%）を充填済。academic-outcomes-db には専用 4-phase ETL が稼働する。OpenAlex を学術ドメインの正本層として活用し、本エコシステムは意味構造（subfield / 系譜 / 概念関係）を担う住み分けにある。

**Karpathy LLM Wiki（2024 提案）と WeKnora（Tencent）** は、LLM-maintained / self-evolving / multi-agent retrieval という方向性を示した。本エコシステムは個人運用という制約下で、167 独立 DB × 各 DB 専属エージェント × cross_db_refs（DB あたり 10+ 件必須）という構成でこの方向性を実装している。

**MLflow Prompt Registry / OpenAI Agents SDK** は、プロンプト・モデル・エージェント定義を成果物として版管理する方向性を提示している。本エコシステムは AR-DB を、これら成果物管理ではなく「エージェント生態系全体の構造的メタ層」として位置づけた。エージェント間の calls / orchestrates / aggregates / extends / observed_by / governed_by 等 9 種の関係型を SQL で照会可能にし、ダッシュボードを赤白 CI HTML で自動生成する。

これら先行事例の地平に立ったうえで、本エコシステムの特徴は「単一構造の新規性」ではなく「**運用規律の組合せ密度**」にある。具体的には、DB 単位の IRR Cohen's Kappa 公表（PHYS 0.87 / CEH 0.99 / ES 0.96 / BOT 0.86）、source_url 100% 必須化、path-1 ルール（LP as truth）、3 経路必須提示（/adb / /db-blindspot / /ddb）、meta-principles-enforcer によるルール監視。個々の要素はいずれも他所に類例があるが、1 個人 + LLM 運用環境でこれらを同時運用する密度は市場の主流（runtime tracing 偏重 / 単一グラフ偏重）から見て uncommon である。

世界初を主張するのは適切ではない。最も誠実な記述は、「先行事例が拓いた地平に立ち、Claude Code + ローカルファイル運用という特殊な環境に固有の運用規律として翻訳した実装」である。この立ち位置こそが、ConceptNet・AWS Agent Registry・ChatDev・OpenAlex・WeKnora と並びうる輪郭を持つ。

---

## 引用先行事例

- [ConceptNet 5.5 (Speer et al., AAAI 2017)](https://arxiv.org/abs/1612.03975)
- [AWS Agent Registry Preview (2024)](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/)
- [ChatDev (OpenBMB)](https://github.com/OpenBMB/ChatDev)
- [AgentOrchestra (arXiv 2506.12508)](https://arxiv.org/html/2506.12508v1)
- [OpenAlex (Priem et al., 2022)](https://arxiv.org/abs/2205.01833)
- [Karpathy LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [WeKnora (Tencent)](https://github.com/Tencent/WeKnora)
- [MLflow Registry](https://mlflow.org/docs/latest/genai/tracing/)
- [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents)
