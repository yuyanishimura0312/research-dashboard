# イノベーション学術知識DB構築 — リサーチ統合レポート

**調査日**: 2026-05-01
**目的**: データ駆動型イノベーション構築に向けた、イノベーション学術知識DBの設計基盤リサーチ
**重点**: シュンペーターの認知的枠組み、産業との関係

## 1. 調査概要

4チームによる並列リサーチを実施。

- **チーム1**: シュンペーター派イノベーション理論（認知的枠組み）
- **チーム2**: 現代イノベーション理論（産業応用重視）
- **チーム3**: イノベーションの測定・定量化・データ駆動型イノベーション
- **チーム4**: 既存miratuku-news-v2 DB群（29DB）の構造分析

## 2. シュンペーター派の認知的枠組み（チーム1）

### 2.1 シュンペーター自身の体系

**5つのイノベーション類型**（『経済発展の理論』1912年）:
1. 新製品の開発
2. 新しい生産方法
3. 新しい原材料・供給源の発見
4. 新しい市場の開拓
5. 新しい組織形態の創設

**創造的破壊**（『資本主義・社会主義・民主主義』1942年）: 新しいイノベーションが古い技術・組織・産業を破壊し、新産業を創出する動的過程。

**Mark I vs Mark II**: 初期は小規模起業家による個人的ビジョン（Mark I）、後期は大企業の組織的R&D（Mark II）へ。

**認知的前提**: 起業家は「見える」のではなく「創造する」。機会は既存ではなく、想像的未来予想と資源の再組み合わせを通じて創造される（creative response）。合理的計算ではなく、ビジョン・想像力・直感に基づく。

### 2.2 ネオ・シュンペーター派

| 研究者 | 主要貢献 | 主要著作 |
|---|---|---|
| Nelson & Winter | 進化経済学、ルーティン理論 | An Evolutionary Theory of Economic Change (1982) |
| Chris Freeman | 国家イノベーションシステム、SPRU設立 | Technology Policy and Economic Performance (1987) |
| Carlota Perez | テクノ経済パラダイム、長期波動 | Technological Revolutions and Financial Capital (2002) |
| Giovanni Dosi | 技術パラダイムと技術トラジェクトリ | Research Policy 11(3), 1982 |
| Malerba & Orsenigo | 技術レジーム、セクター別イノベーション | Industrial and Corporate Change 6(1), 1997 |
| Lundvall | 国家イノベーションシステム（学習と相互作用） | National Systems of Innovation (1992) |

### 2.3 認知的枠組みの階層構造

- **個人レベル**: 起業家的ビジョン（Schumpeter）、警戒性（Kirzner）、認知バイアス（Christensen）
- **組織レベル**: ルーティン（Nelson & Winter）、パス依存性、知識基盤
- **セクターレベル**: 技術パラダイム（Dosi）、技術レジーム（Malerba）、優位設計（Utterback & Abernathy）
- **システムレベル**: NIS（Freeman/Lundvall/Nelson）、テクノ経済パラダイム（Perez）

## 3. 現代イノベーション理論（チーム2）

### 3.1 オープンイノベーション系

| 理論 | 研究者 | 年 | 核心概念 |
|---|---|---|---|
| Open Innovation | Chesbrough | 2003 | 組織内外の知識フローの戦略的管理 |
| User Innovation | von Hippel | 1986 | リードユーザーが革新の源泉 |
| Platform Innovation | - | 2010s | エコシステムとしてのイノベーション |

### 3.2 破壊的イノベーション系

| 理論 | 研究者 | 年 | 核心概念 |
|---|---|---|---|
| Disruptive Innovation | Christensen | 1997 | 低性能・低価格技術による市場侵食 |
| Architectural Innovation | Henderson & Clark | 1990 | 既存部品の新たな組み合わせ |
| Competence-Destroying Discontinuity | Tushman & Anderson | 1986 | 既存スキルを無効化する技術変化 |
| Ambidexterity | O'Reilly & Tushman | 1990s | 既存事業の深耕と新規事業の探索の両立 |

### 3.3 プロセス理論

| 理論 | 研究者 | 年 | 核心概念 |
|---|---|---|---|
| Stage-Gate | Cooper | 1980s | 段階的ゲート判定による新製品開発管理 |
| Design Thinking | IDEO/Stanford | 2000s | 人間中心の反復的問題解決 |
| Lean Startup | Ries | 2011 | MVP + Build-Measure-Learn |
| Effectuation | Sarasvathy | 2001 | 手段ベース・許容喪失原則の起業家的推論 |

### 3.4 制度・システム理論

| 理論 | 研究者 | 年 | 核心概念 |
|---|---|---|---|
| National Innovation Systems | Freeman/Lundvall/Nelson | 1987-93 | 技術の創造・普及に関わる公私機関ネットワーク |
| Triple Helix | Etzkowitz & Leydesdorff | 1998 | 大学・産業・政府の三者相互作用 |
| Innovation Ecosystems | Adner | 2010 | ステークホルダー間の技術的相互依存構造 |
| Mission-Oriented Innovation | Mazzucato | 2013 | 政府を能動的価値創造者として位置づけ |

### 3.5 知識・学習理論

| 理論 | 研究者 | 年 | 核心概念 |
|---|---|---|---|
| Absorptive Capacity | Cohen & Levinthal | 1990 | 外部知識を認識・同化・応用する組織能力 |
| SECI Model | Nonaka & Takeuchi | 1995 | 暗黙知-形式知の4モード螺旋的変換 |
| Communities of Practice | Wenger | 1998 | 社会的共同参加による学習 |
| Dynamic Capabilities | Teece, Pisano & Shuen | 1997 | センシング・シージング・トランスフォーミング |

## 4. イノベーションの測定・定量化（チーム3）

### 4.1 国際測定フレームワーク

- **Oslo Manual** (OECD, 4th ed. 2018): イノベーション調査の国際標準。4類型定義
- **European Innovation Scoreboard**: 32指標、4階層評価
- **Global Innovation Index** (WIPO): 80指標、139経済圏、2025年版ではGII-iLens Data Lab

### 4.2 セクトラルパターン

- **Pavitt Taxonomy** (1984): サプライヤー主導型、規模集約型、専門供給者型、科学基盤型
- 2016年にBogliacino & PiantaがICT拡張版を提案
- 2008年CastellacciがサービスセクターとR統合

### 4.3 技術ライフサイクル

- **S曲線**: 技術パフォーマンスの成長段階
- **Hype Cycle** (Gartner): 期待値のダイナミクス（5段階）
- **Bass Diffusion Model**: 革新係数(p)と模倣係数(q)による普及予測

### 4.4 データ駆動型イノベーション（DDI）

- **OECD DDI Framework** (2015): データがR&Dと同等のイノベーション駆動要因
- プラットフォームデータ共有の4アーキタイプ
- 生成AIをGeneral Purpose Technologyとして評価（OECD 2025）

### 4.5 最新トレンド

- Responsible Innovation / Sustainability-Oriented Innovation
- Frugal Innovation（第四の波 — 規範的中核への進化）
- Social Innovation Measurement（SROI, SIMPLE methodology）
- AI as GPT: OECD基準（普遍性・継続的改善・イノベーション誘発）充足

## 5. 既存DB群との接続設計（チーム4）

### 5.1 miratuku-news-v2 DB構造

29DB、15.2M+レコード、4層アーキテクチャ。

### 5.2 直接接続先（10DB）

```
Innovation DB (新規)
  ├── TA (技術発展加速度DB, 227Kレコード) — 技術パラダイム・S曲線の実証データ
  ├── GPT-QoL (汎用技術×QoL, 34,715事象) — 創造的破壊の産業横断分析
  ├── SIF (SI歴史的構造変革DB, 1,096事象) — 社会的イノベーション事例
  ├── GF (歴史構造DB, 9,178人物) — 起業家的行為者の歴史的事例
  ├── SG (シグナルDB, 7,668件) — 現在進行中のイノベーションシグナル
  ├── SI (企業ニーズDB, 492,646レコード) — 産業現場のイノベーション需要
  ├── IR (VC投資DB, 4,180組織) — 投資パターンと技術レジーム対応
  ├── PD (政策DB, 221,788行) — NIS/ミッション志向型政策の実態
  ├── AD (AI発展DB, 2,236論文) — AIをGPTとして捉える分析基盤
  └── FK (フォーサイト知識基盤, 45,323レポート) — フォーサイトとイノベーション交差
```

## 6. DB設計方針

### 6.1 三層認知モデル（シュンペーター認知的枠組み軸）

**層1: 認知・行為者層（Micro）** — なぜイノベーションは「見える」のか
- 起業家的認知、知識創造、意思決定ロジック、認知バイアス

**層2: 産業・技術層（Meso）** — イノベーションはどう展開するか
- 技術パラダイム、技術レジーム、産業ライフサイクル、破壊と再構成

**層3: システム・制度層（Macro）** — イノベーションの生態系
- NIS、テクノ経済パラダイム、Triple Helix、エコシステム、測定・評価

### 6.2 提案スキーマ（10テーブル）

1. **theories** — イノベーション理論（~150件）
2. **researchers** — 研究者（~300人）
3. **works** — 主要論文・著作（~800件）
4. **concepts** — 核心概念（~400件）
5. **industries** — 産業セクター分類（Pavitt + ISIC拡張）
6. **mechanisms** — イノベーションメカニズム（5類型×転換パターン）
7. **paradigm_shifts** — 技術パラダイム転換事例（~200件、TA/GPT接続）
8. **measurements** — 測定フレームワーク・指標
9. **relations** — 理論間・概念間の関係ネットワーク
10. **cross_domain** — 既存DB群との接続テーブル

### 6.3 推定規模

- 理論: ~150件
- 研究者: ~300人
- 文献: ~800件
- 概念: ~400件
- 関係: ~1,500件
- 合計: ~3,000+ レコード（初期）

## 7. 次のステップ（選択肢）

**A案**: /academic-db パイプライン適用（Phase 0→1→2→3）
**B案**: 統合理論構築先行、過程でDB蓄積

**判断事項**:
1. スコープ重点: シュンペーター派深掘り vs 全理論網羅
2. 産業軸: 特定産業焦点 vs 全産業横断
3. 目的: 実践フレームワーク vs 学術的知識体系

---

*Generated by 4-team parallel research, 2026-05-01*
