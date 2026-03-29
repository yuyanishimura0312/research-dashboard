# PESTLE分析と因果階層分析（CLA）を統合した未来洞察の方法論とシステム設計：調査レポート

作成日: 2026年3月29日

---

## 1. PESTLEとCLAを組み合わせた分析フレームワークの提案

PESTLEとCLAの明示的な統合フレームワークを単独で提案した学術論文は、現時点では確認できなかった。しかし、両手法は構造的に強い補完関係にあり、実務・学術の両面で暗黙的な統合が進んでいる。

Sohail Inayatullahが提唱した「Six Pillars」フレームワークは、フォーサイトプロセスを6つの柱（mapping, anticipating, timing, deepening, creating alternatives, transforming）で構成する。この中で、CLAは「deepening（深化）」の柱に位置づけられ、STEEP/PESTLE分析は「mapping（地図化）」や「anticipating（予測）」の段階で用いられる。つまり、PESTLEで水平的に収集・分類した環境情報を、CLAで垂直的に深掘りするという階層的な接続が、Inayatullahのフレームワーク内で既に想定されている。

CLAの4層構造（Litany → Social/Systemic Causes → Worldview/Discourse → Myth/Metaphor）において、PESTLE分析は主にLitany層（表層的な事象の把握）とSocial/Systemic Causes層（社会的・構造的原因の分析）に対応する。PESTLEの各カテゴリ（政治・経済・社会・技術・法的・環境）で収集された情報は、CLAの上位2層を構成する「素材」として機能し、そこからWorldview層やMyth/Metaphor層への深掘りへと接続される。

UNDPのForesight CPD Toolkitでも、ホライゾンスキャニング（STEEPフレームワーク使用）とCLAは同一のフォーサイトプロセスの中で順次適用されるツールとして位置づけられている。UNDPは特にCLAワークショップを通じて「表層的な課題と深層的・構造的な障壁の両方に対処する」ことを重視している。

**出典:**
- [Six Pillars: Futures Thinking for Transforming - Inayatullah (2008)](https://www.metafuture.org/library1/FuturesStudies/Six-pillars-Foresight-2008.pdf)
- [Six Pillars Model Summarised - Metafuture](https://www.metafuture.org/2015/11/18/six_pillars/)
- [UNDP Foresight CPD Toolkit - CLA for Programme Design](https://www.undp.org/future-development/foresight-cpd-toolkit/chapter-3-foresight-programme-design/chapter-3-foresight-programme-design/causal-layered-analysis-programme-design)
- [CLA - UN Global Pulse Foresight Project](https://foresight.unglobalpulse.net/blog/tools/causal-layered-analysis/)
- [Causal Layered Analysis - Wikipedia](https://en.wikipedia.org/wiki/Causal_layered_analysis)


## 2. 日次のPESTLE分析から月次のCLAへの接続方法論

日次PESTLE分析を月次CLAに体系的に接続する具体的な方法論を記述した文献は見当たらなかったが、既存のフォーサイト実務から合理的な接続パターンを構築できる。

環境スキャニングの頻度について、実務上は「fast-movingな産業では四半期ごと、安定的な環境では年次」が一般的とされているが、戦略的フォーサイトは「一度きりのイベントではなく、通常の戦略策定プロセスの一部」であるべきとされている。Boston Consulting Groupのコンサルタントは、弱いシグナルが明確なパターンになる前に察知する「継続的日次スキャニング」の重要性を強調している。

接続の方法論として考えられるのは、日次のPESTLEスキャニングで収集した個別シグナルを、月次でCLAの4層に整理し直すアプローチである。具体的には、日次で収集されたニュース記事やシグナルをPESTLEカテゴリで分類・蓄積し、月次のCLAワークショップ（またはその自動化版）で、蓄積されたシグナル群をLitany層として整理した上で、Social/Systemic層でパターンやトレンドを抽出し、Worldview層で支配的なナラティブや前提を特定し、Myth/Metaphor層で深層の文化的物語を探索する、という階層的深化プロセスである。

ITONICSのフォーサイトプラットフォームでは「scan → synthesize → model scenarios → set signposts → integrate into planning」というワークフローが推奨されており、スキャニング（日次的）からシナリオモデリング（月次〜四半期的）への接続が実務的に確立されている。

**出典:**
- [How PESTLE Analysis Helps Organizations Move from Reactive to Strategic](https://www.inclusiongeeks.com/how-pestle-analysis-helps-organizations-move-from-reactive-to-strategic/)
- [ITONICS: Effective Environment Scanning](https://www.itonics-innovation.com/blog/environment-scanning)
- [Trendtracker: How to Develop Strategic Foresight](https://www.trendtracker.ai/blog-posts/how-to-develop-strategic-foresight-through-environmental-scanning)
- [OECD OPSI: Futures and Foresight](https://oecd-opsi.org/guide/futures-and-foresight/)


## 3. ニュースデータの自動収集・分類・分析パイプラインの設計パターン

ニュースデータを自動収集し、PESTLEカテゴリに分類するパイプラインは、既存のNLP技術とデータエンジニアリングパターンの組み合わせで実現可能である。

パイプラインの基本構成は、データ収集層（RSS/API経由のニュース取得）、前処理層（テキストクリーニング、Unicode正規化、ストップワード除去、ステミング）、分類層（PESTLE 6カテゴリへの分類）、分析層（トレンド検出、センチメント分析、弱いシグナル抽出）、蓄積・可視化層（時系列データベースへの格納とダッシュボード表示）から成る。

AI搭載のPESTLE分析ツールは既に「ニュースアウトレット等の複数ソースからデータを収集し、高度なアルゴリズムでパターンを識別して関連するインサイトを抽出する」ことが可能とされている。機械学習ベースのニュースカテゴリ分類システムは、アンサンブル分類器と文字列前処理パイプラインを用い、ラベル付きデータとラベルなしデータの両方を処理する。

Shaping Tomorrowのプラットフォームは、約10万の信頼性のあるソースからニュースを収集し、自動的に集約・重複排除した上でフォーサイト分析に供するアーキテクチャを採用している。Futures Platformは「経験豊富なフォーサイト専門家が手作業でキュレーション」するモデルを維持しており、完全自動化と人間によるキュレーションの中間モデルが実務上は最も信頼されている。

ファインチューニングされたLLMを用いた場合、約1,000記事/カテゴリのラベル付きデータで学習させたモデルは、キーワードマッチングによるルールベース分類と比較して「明らかに優れた品質」を達成するという報告がある。

**出典:**
- [LLMs for Innovation and Technology Intelligence - Mapegy Tech (Medium)](https://medium.com/mapegy-tech/llms-for-innovation-and-technology-intelligence-news-categorization-and-trend-signal-detection-ec4171627937)
- [How to Create a PESTLE Analysis Using AI](https://pestleanalysis.com/how-to-create-a-pestle-analysis-using-ai/)
- [Pipeline Design for Data Preparation for Social Media Analysis (ACM)](https://dl.acm.org/doi/10.1145/3597305)
- [Shaping Tomorrow - Your Horizon Scanning Platform](https://www.shapingtomorrow.com/text/your-futures-foresight-platform)
- [Futures Platform](https://www.futuresplatform.com/)


## 4. Weak Signals（弱いシグナル）の検出手法とPESTLE分類への接続

弱いシグナル検出は、フォーサイト研究における中核的な方法論の一つであり、近年はAI・NLP技術の進展により自動化が急速に進んでいる。

弱いシグナルの定義として、「現在の頻度は低いが成長率が高い情報断片であり、3〜5年のスパンで重要な変化の前兆となりうるもの」とされている。PESTLEフレームワークはこの弱いシグナルの分類体系として「完璧な出発点」と位置づけられており、スキャニング活動で収集されたシグナルをPESTLEの6カテゴリに分類することが推奨されている。

WISOMフレームワーク（2024年発表）は、AI搭載の弱いシグナル検出手法として注目に値する。BERTopicによるトピックモデリング、T5モデルによる自動ラベリング、そしてTopic Emergence Maps（TEM）による可視化を組み合わせている。TEMは平均トピック比率と成長率の2軸でトピックを4象限（Strong Signal、Weak Signal、Latent Signal、Known-but-not-Strong Signal）に分類する。

BERTrend（2024年発表、RTE France開発）は、BERTopicをオンライン学習設定で適用し、トピックの「人気度メトリクス」（文書数と更新頻度の複合指標）に基づいてノイズ・弱いシグナル・強いシグナルを動的に分類する。50パーセンタイル超を強いシグナル、10〜50パーセンタイルで上昇傾向のものを弱いシグナル、それ以下をノイズとする閾値を用い、指数関数的減衰による「忘却ゲート」メカニズムで陳腐化したシグナルの影響を排除する。BERTrendはオープンソース（GitHub/PyPI）で利用可能である。

韓国の研究グループによる「キーワードネットワーククラスタリングとグラフ畳み込みネットワークを用いた弱いシグナル検出・予測の自動化」(2023年、Futures誌掲載)も、NLPとグラフニューラルネットワークの組み合わせによる先進的アプローチを示している。

**出典:**
- [WISDOM: An AI-powered Framework for Emerging Research Detection (arXiv)](https://arxiv.org/html/2409.15340v1)
- [BERTrend: Neural Topic Modeling for Emerging Trends Detection (arXiv)](https://arxiv.org/html/2411.05930v1)
- [BERTrend - GitHub (RTE France)](https://github.com/rte-france/BERTrend)
- [Automated Weak Signal Detection and Prediction Using Keyword Network Clustering and GCN (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0016328723001064)
- [ITONICS: How to Accelerate Weak Signal Detection](https://www.itonics-innovation.com/blog/how-to-accelerate-weak-signal-detection)
- [Futures Signals Sense-making Framework (FSSF) - ResearchGate](https://www.researchgate.net/publication/247150625_Futures_signals_sense-making_framework_FSSF_A_start-up_tool_to_analyse_and_categorise_weak_signals_wild_cards_drivers_trends_and_other_types_of_information)


## 5. 環境スキャニングからシナリオ構築への接続方法

環境スキャニングからシナリオ構築への接続は、フォーサイト研究において最も確立された方法論的連結の一つである。

Springerに掲載されたGausemeier et al.の方法論は、PESTLEを用いたシナリオ構築の標準的な手順を提示している。第1段階でスコープと意思決定領域を定義し、第2段階でPESTLEの6次元に沿って主要なトレンドを特定する。第3段階でトレンドを「記述子（Descriptor）」と呼ばれる中立的な未来トピックに変換し、それぞれの記述子に対して複数の「将来予測（Future Projection）」を作成する。第4段階でクロスインパクト・マトリクスにより将来予測の整合性を評価し、整合的な予測の束を「シナリオ候補」として構成する。第5段階で定性的な妥当性検証を経て最終シナリオを確定する。

Morrison (UNC) による「Developing Scenarios: Linking Environmental Scanning and Strategic Planning」は、環境スキャニングレポートからシナリオへの変換プロセスを記述した古典的文献であり、スキャニングで特定された重要シグナルをシナリオの「不確実性の軸」に変換する方法論を提示している。

Clemens & Jonesの「Environmental Scanning and Scenario Planning: A 12 month Perspective on Applying the Viable Systems Model」（Systemic Practice and Action Research, 2009）は、実行可能システムモデル（VSM）を用いて環境スキャニングとシナリオ計画を12か月のサイクルで接続した公共部門での実践事例を報告している。

OECD OPSI のフォーサイトガイドでは、Perceiving（認知）→ Sense-making（意味づけ）→ Acting（行動）の3段階反復プロセスが示されており、ホライゾンスキャニングで検出されたシグナルがメガトレンド分析とシナリオ計画を経て戦略的意思決定に接続される。

**出典:**
- [A Methodology for Future Scenario Planning (Springer)](https://link.springer.com/chapter/10.1007/978-3-030-63505-3_2)
- [Developing Scenarios: Linking Environmental Scanning and Strategic Planning - SCUP](https://www.scup.org/resource/developing-scenarios-linking-environmental-scanning-and-strategic-planning/)
- [Environmental Scanning and Scenario Planning - Viable Systems Model (Springer)](https://link.springer.com/article/10.1007/s11213-009-9127-y)
- [OECD OPSI: Futures and Foresight](https://oecd-opsi.org/guide/futures-and-foresight/)
- [Exploring Futures through Science Fiction: A Scenario-based PESTLE Analysis (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0016328725001090)


## 6. LLM（GPT/Claude）を使ったPESTLE自動分類の精度に関する研究

PESTLE分類に特化したLLMベンチマーク研究は現時点では確認できなかったが、関連するテキスト分類タスクでのLLMの性能に関する知見は蓄積されている。

LLMによるテキスト分類全般について、GPT-4.5とClaude 3.7 Sonnetは金融苦情分類タスクにおいてそれぞれ0.774と0.765の精度を達成した。医学分野の評価ではClaude 3.7が95%、DeepSeekが93%、ChatGPTが90%の精度を記録している。ゼロショット設定でのツイートからのテキスト抽出では基準精度19%だったが、few-shotプロンプトエンジニアリングにより97%まで向上した事例も報告されている。

反復的プロンプトエンジニアリングによる分類性能の改善は14%〜32%の範囲であるとする研究がある（Claude 2.0を使用した事例、ScienceDirect掲載）。

重要な注意点として、LLMの分類タスクでの「真の理解」は適切に評価されていないという指摘がある。正解選択肢が利用可能な場合は高い精度を示すが、正解が存在しない場合には「正解がない」ことを認めることに抵抗するという挙動が確認されている。これはPESTLE分類において、複数カテゴリにまたがる記事や分類困難な記事の処理に影響を与える可能性がある。

Mapegy Techの実務報告では、ファインチューニングしたLLMによるニュースカテゴリ分類が、キーワードマッチングのルールベース手法を「明らかに上回る」精度を達成したとされている。約1,000記事/カテゴリの学習データでこの水準に達しており、PESTLE分類への応用可能性は高い。

eコマース製品分類に関するScienceDirectの比較研究（2025年）では、GPT-4o、GPT-4o mini、Claude 3.5 Sonnet、Claude 3.5 Haikuがゼロショット設定で評価され、モデル間で有意な精度差があり、特定のモデルが実世界アプリケーションでの拡張性と適応性に優れることが示された。

**出典:**
- [LLMs for Product Classification in E-commerce (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2949719125000184)
- [Claude 2.0: Tackling Classification with Iterative Prompt Engineering (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2667305324000127)
- [LLMs' Classification Performance is Overclaimed (arXiv)](https://arxiv.org/html/2406.16203v1)
- [LLMs for Innovation and Technology Intelligence - Mapegy Tech (Medium)](https://medium.com/mapegy-tech/llms-for-innovation-and-technology-intelligence-news-categorization-and-trend-signal-detection-ec4171627937)
- [Best Model for Text Classification: Gemini Pro, GPT-4 or Claude2? (Vellum.ai)](https://vellum.ai/blog/best-at-text-classification-gemini-pro-gpt-4-or-claude2)
- [Text Classification With LLMs: A Roundup (Striveworks)](https://www.striveworks.com/blog/text-classification-with-llms-a-roundup-of-the-best-methods)


## 7. 時系列でのPESTLEトレンド変化の可視化手法

PESTLEカテゴリ別のトレンド変化を時系列で可視化する手法は、フォーサイトソフトウェア業界で実用化が進んでいる。

トレンドレーダー（Trend Radar）は、フォーサイト可視化の代表的な手法である。ITONICS、Futures Platform、FIBRES、Trendtrackerなどのプラットフォームが提供するレーダー型ビジュアライゼーションは、トレンドデータを4次元で可視化し、PESTLEカテゴリをセクター（扇形領域）として表示できる。レーダーのリングは「インパクトまでの時間」「成熟度」「戦略的重要度」「暦年」などで設定可能であり、弱いシグナルから強いトレンドへの推移を視覚的に追跡できる。

ITONICSのRadarは「ランク付けされたトレンドとPESTLEビュー」を提供し、発見プロジェクトやポートフォリオレビューの優先順位付けを容易にしている。

時系列データの可視化ベストプラクティスとしては、折れ線グラフ（トレンド表示）、面グラフ（構成比の変遷）、散布図（異常値検出）、ヒートマップ（カテゴリ横断の強度変化）が主要な手法である。各チャートは「一つの主要なインサイト」を伝達することに集中すべきとされ、複数のインサイトには別個のビジュアライゼーションを用いることが推奨されている。

Daan de Geusの「PESTLE Analysis Visualization」（Medium掲載）は、PESTLEカテゴリ別の可視化にGenerative AI を活用して戦略的インサイトをより魅力的にする手法を紹介している。

ダッシュボード設計では、F字型の視線パターンを考慮し、左上に最も重要なグローバル数値や指標を配置することが推奨される。戦略ダッシュボードはKPIのトラッキングに特化し、「より少なく、より大きなチャート」で構成される。特定のイベント（製品発表、障害等）にアノテーションを付けることで、データの急変を解釈しやすくすることが重要とされている。

**出典:**
- [PESTLE Analysis Visualization (Medium - Daan de Geus)](https://medium.com/@daandegeus/pestle-analysis-visualization-2f694b2f629f)
- [ITONICS: Radar Software for Foresight Management](https://www.itonics-innovation.com/radar)
- [ITONICS: Trend Radar Tools & Software](https://www.itonics-innovation.com/trend-radar)
- [FIBRES - Trend Radar Builder](https://www.fibresonline.com/features/trend-radar)
- [Trendtracker: Real-Time Trend Radar](https://www.trendtracker.ai/platform/features/trend-radar)
- [Valona Intelligence: Foresight Trend Radars](https://valonaintelligence.com/market-intelligence-software/foresight-trend-radars)
- [Metabase: How to Visualize Time-Series Data](https://www.metabase.com/blog/how-to-visualize-time-series-data)


## 8. テキストマイニングによるWorldview/Discourse層の自動分析

CLAのWorldview/Discourse層およびMyth/Metaphor層の自動分析は、NLP・テキストマイニング研究の最前線に位置する課題である。

「Mapping Technological Futures: Anticipatory Discourse Through Text Mining」（Nature Humanities and Social Sciences Communications, 2025年）は、この分野で最も関連性の高い研究である。Xプラットフォーム上の400人のキーオピニオンリーダーによる150万件の投稿（2021〜2023年）を、BERTopicモデリング、センチメント分析、感情分析、態度分析を組み合わせて解析し、技術主導の将来像を反映する100の異なるトピックを特定した。この研究は「予期的言説（anticipatory discourse）」をテキストマイニングで体系的に捕捉する先駆的アプローチを示している。

トピックモデリングはマクロレベルでの「テーマクラスター」の発見に有効であり、テキスト分類はミクロレベルでの「政治的スタンスの言説」の追跡に有効である。データ駆動型クラスタリングと理論駆動型分類の組み合わせにより、大規模テキストコレクションに対する複雑な分析ワークフローが可能になる。

Worldview層の自動検出については、政治的言説におけるメンタルモデルの研究が参考になる。個人の知覚、視点、世界観は異なるメンタルモデルとして表現され、自動テキストツールが人間と同等の概念抽出を行えるかを検証する研究が進んでいる。

Myth/Metaphor層については、計算論的メタファー処理技術のサーベイ（Artificial Intelligence Review掲載）が、メタファーの「識別・解釈・生成・応用」にわたる技術の包括的レビューを提供している。CLAのMith/Metaphor層は「世界観（フレーム）のレベルの下に存在する、概念的思考体系を緩やかに組織化するイメージ」であり、言語と想像の空間に存在するメタファーやイメージを探索するものとされている。この層の完全な自動化は現時点では困難であるが、メタファー検出技術の進展により部分的自動化は視野に入りつつある。

Journal of Futures Studies (2022年)に掲載された「Living Between Myth and Metaphor: Level 4 of Causal Layered Analysis Theorised」は、CLAの第4層（Myth/Metaphor）の理論的基盤を精緻化した論文であり、この層の分析手法の体系化に貢献している。

**出典:**
- [Mapping Technological Futures: Anticipatory Discourse Through Text Mining (Nature)](https://www.nature.com/articles/s41599-025-05083-5)
- [Text Mining for Discourse Analysis (Springer)](https://link.springer.com/chapter/10.1007/978-3-319-97370-8_7)
- [Unveiling Global Discourse Structures: NLP Applications in Argument Mining (arXiv)](https://arxiv.org/html/2502.08371v1)
- [A Survey on Computational Metaphor Processing Techniques (ACM/Springer)](https://dl.acm.org/doi/10.1007/s10462-023-10564-7)
- [Living Between Myth and Metaphor: Level 4 of CLA Theorised (Journal of Futures Studies)](https://jfsdigital.org/2022-2/vol-27-no-2-december-2022/living-between-myth-and-metaphor-level-4-of-causal-layered-analysis-theorised/)
- [Text Mining Applications in Discourse Analysis (ResearchGate)](https://www.researchgate.net/publication/375457009_Text_Mining_Applications_in_Discourse_Analysis_and_Modern_Trends_Bid_Data_Methods_on_Political_Speeches)


## 9. フォーサイトダッシュボードのUI/UXベストプラクティス

フォーサイトダッシュボードは「戦略ダッシュボード」のサブカテゴリに位置づけられ、長期的なKPIトラッキングと変化の兆候の可視化を主目的とする。

ダッシュボード設計の基本原則として、視覚的階層性（Visual Hierarchy）が最重要とされている。レイアウト、色彩、タイポグラフィを戦略的に活用し、F字型の視線パターンに沿って最も重要な情報を左上に配置する。初期画面には最も関連性の高い情報のみを表示し、詳細データへのドリルダウンを可能にする設計が推奨される。

データストーリーテリングの観点からは、KPIを「物語を語るように」配置し、重要な指標を強調した上で、過去の四半期データやブレイクダウンを小さいフォントで提示する手法が有効とされている。指標は常にベースラインとの比較で表示し、特定のイベントにはアノテーションを付けてデータの急変を解釈可能にすべきである。

フォーサイト固有のUI/UXとしては、トレンドレーダー（ITONICS, Futures Platform, FIBRES等が採用）が業界標準の可視化パターンとなっている。同心円のリングと扇形のセクターで時間軸とカテゴリ軸を表現し、個別のシグナルやトレンドをプロットする。インタラクティブ性が重視され、ウェブページやイントラネットへの埋め込み、フィルタリング、ドリルダウンが標準機能として提供されている。

意思決定中心のダッシュボード設計では、組織の目標とアカウンタビリティの連鎖を反映し、「意思決定の瞬間（decision moments）」をマッピングすることが推奨されている。各KPIは測定可能なビジネス目標に紐づけられるべきであり、データの可視化は意思決定の改善に直結する設計でなければならない。

Ross Dawsonによるフォーサイトソフトウェアの比較分析では、ITONICS（統合的フォーサイト管理と高度なビジュアルインターフェース）、Futures Platform（専門家キュレーションによるトレンドデータベース）、Shaping Tomorrow（AI搭載のホライゾンスキャニング）が主要プラットフォームとして挙げられている。

**出典:**
- [Dashboard Design Best Practices (Justinmind)](https://www.justinmind.com/ui-design/dashboard-design-best-practices-ux)
- [Dashboard Design Principles (UXPin)](https://www.uxpin.com/studio/blog/dashboard-design-principles/)
- [Dashboard UI Design: 14 Best Practices (Adam Fard Studio)](https://adamfard.com/blog/dashboard-ui)
- [Dashboard Design: Best Practices (Toptal)](https://www.toptal.com/designers/data-visualization/dashboard-design-best-practices)
- [ITONICS: Foresight Software](https://www.itonics-innovation.com/foresight)
- [Futures Platform](https://www.futuresplatform.com/)
- [Overview of Futurist and Foresight Software (Ross Dawson)](https://rossdawson.com/analysis-futurist-foresight-software-tools/)


## 10. Strategic Foresight Processのフレームワーク（OECD, UNESCO, UNDP等）

国際機関によるStrategic Foresightフレームワークは、複数の体系的アプローチが並行して発展している。

OECDは2025年に「Strategic Foresight Toolkit for Resilient Public Policy」を公表した。5段階のプロセス（(1) 将来の潜在的混乱の探索、(2) システム的相互作用の想像、(3) シナリオの作成、(4) シナリオに基づくビジョン策定と戦略立案、(5) 新たな政策の提言）で構成される。環境・技術・経済・社会・地政学の5領域にわたる25のエビデンスベースの潜在的混乱要因を探索し、2030〜2050年の政策ランドスケープを展望する。

OECD OPSIの「Futures and Foresight」ガイドは、3段階の反復プロセスとしてPerceiving（認知：ホライゾンスキャニング、デスクリサーチ、テキストマイニング）、Sense-making（意味づけ：メガトレンド分析、シナリオ計画、CLA、システムモデリング）、Acting（行動：ビジョニング、ウィンドトンネリング、戦略オプションキャンバス）を提示している。重要なのは、この3段階が「順次的ステップではなく、相互に情報を提供し合う恒常的な反復プロセス」であると明記されている点である。CLAはSense-makingフェーズの推奨ツールに含まれている。

OECD は2025年に「Building Anticipatory Capacity with Strategic Foresight in Government」も公表しており、政府組織における先見的能力の構築方法を体系化している。

UNESCOは「Futures Literacy」の概念を中核に据えたフレームワークを展開している。Futures Literacy Laboratories（FLL）は、学習、実験室、集合知、予測の4つの理論的支柱に基づく参加型プロセスであり、Probable（蓋然的）、Preferable（望ましい）、Reframed（再構成された）の3種類の未来を探索する。マスタークラスではホライゾンスキャニング、シナリオ、スペキュラティブ・フューチャーズ、システム変革のためのフォーサイトが教授されている。

UNDPは「Foresight CPD Toolkit」を通じて、ホライゾンスキャニング（STEEPフレームワーク）とCLAを統合したプロセスを実践している。UNDPの「Future Trends & Signals System（FTSS）」は、グローバルおよび地域のソースからキュレーションされたトレンドとシグナルのリポジトリであり、組織内の同僚が変化のシグナルを観察・記録・共有するために設計されたシステムである。FTSSは日常的なスキャニングからCLAワークショップ、バックキャスティング、プログラム設計へと接続するワークフローの入口として位置づけられている。

Inayatullahの「Six Pillars」フレームワーク（2008年）は、学術的により精緻な方法論として、mapping（フューチャーズ・トライアングル）、anticipating（新興課題分析、フューチャーズ・ホイール）、timing（Polak-Sarkarゲーム）、deepening（CLA）、creating alternatives（シナリオ計画）、transforming（ビジョニング、バックキャスティング）の6柱で構成される。STEEP/PESTLEは主にmappingとanticipatingの段階で使用され、CLAによるdeepening を経てシナリオ構築へと接続される。

**出典:**
- [OECD: Strategic Foresight Toolkit for Resilient Public Policy](https://www.oecd.org/en/publications/foresight-toolkit-for-resilient-public-policy_bcdd9304-en.html)
- [OECD: Strategic Foresight Programme](https://www.oecd.org/en/about/programmes/strategic-foresight.html)
- [OECD OPSI: Futures and Foresight](https://oecd-opsi.org/guide/futures-and-foresight/)
- [OECD OPSI: Playbook for Strategic Foresight and Innovation](https://oecd-opsi.org/toolkits/playbook-for-strategic-foresight-and-innovation/)
- [OECD: Building Anticipatory Capacity with Strategic Foresight in Government](https://www.oecd.org/en/publications/building-anticipatory-capacity-with-strategic-foresight-in-government_d7eb0bb6-en.html)
- [UNESCO: Futures Literacy](https://www.unesco.org/en/futures-literacy)
- [UNESCO Futures Literacy Laboratories Playbook 2023 (ResearchGate)](https://www.researchgate.net/publication/373157930_UNESCO_Futures_Literacy_Laboratories_Playbook_2023_final)
- [UNDP: Foresight CPD Toolkit - Horizon Scanning](https://www.undp.org/future-development/foresight-cpd-toolkit/chapter-1/chapter-1/chapter-1/horizon-scanning)
- [UNDP: Future Trends & Signals System](https://www.undp.org/future-development/foresight-cpd-toolkit/chapter-1/chapter-1/chapter-1/horizon-scanning/undps-future-trends-signals-system)
- [Six Pillars: Futures Thinking for Transforming (ResearchGate)](https://www.researchgate.net/publication/228634731_Six_pillars_Futures_thinking_for_transforming)


---

## 補遺：日本における関連研究

科学技術・学術政策研究所（NISTEP）が開発したKIDSASHI（Knowledge Integration through Detecting Signals by Assessing/Scanning the Horizon for Innovation）は、日本語でのホライゾンスキャニング自動化の先駆的システムである。約300の大学・研究機関からのニュースリリースを自動収集し、機械学習・深層学習で研究分野・内容タイプ・時系列を自動分類する。2016年9月から2019年7月にかけて第11回科学技術予測調査のために変化の兆候情報を収集した。

石垣達也ら（産総研、JAIST、東大、一橋大）による「ホライゾン・スキャニングの自動化のための言語処理応用」（自然言語処理, 2023年）は、新聞記事の大量収集と重要記事の自動抽出（文書探索）、および主観的コメントの自動生成を扱っている。探索モデルは「適合率@100において70%の性能」を達成し、実利用に耐える品質が確認されている。特徴語と意味的距離の観点から一般的記事と異なる文書を識別する手法を採用している。

鷲田祐一らによる「ホライゾン・スキャニング手法による未来洞察活動」（トランスファー, 2019年）は、ホライゾンスキャニングのシナリオ的中度研究を含む、手法の体系的な解説を提供している。

**出典:**
- [NISTEP KIDSASHI概要](https://www.nistep.go.jp/wp/wp-content/uploads/KIDSASHI.pdf)
- [NISTEP ホライズン・スキャニングレポート](https://www.nistep.go.jp/research/science-and-technology-foresight-and-science-and-technology-trends/scanning-reports/)
- [ホライゾン・スキャニングの自動化のための言語処理応用 (J-STAGE)](https://www.jstage.jst.go.jp/article/jnlp/30/3/30_883/_article/-char/ja/)
- [ホライゾン・スキャニング手法による未来洞察活動 (J-STAGE)](https://www.jstage.jst.go.jp/article/trafst/12/2/12_89/_article/-char/ja/)
