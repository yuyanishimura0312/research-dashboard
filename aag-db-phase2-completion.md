# AAG-DB Phase 2 ETL 完了レポート (Wave 1)

**日付**: 2026-05-19
**プロジェクト**: AAG-DB (App Attraction & Growth Knowledge DB) / 人が集まるアプリの学術DB
**経路**: /adb v1.1 Phase 0-15 経路A
**場所**: ~/projects/research/aag-db/

## 起点
「売れるアプリ・ユーザーが集まるアプリ」の学術知見を、単なる事例集ではなく
「人が集まるとはどういうことか」「魅力はどう形成されるか」「具体実装のアルゴリズム・数式」まで
連続的に追跡できる知識基盤として構築。16 サブフィールド・特殊テーブル 8 種で網羅。

## Phase 2 結果

| 区分 | レコード数 | 検証 | 出典URL |
|-----|-----------|------|---------|
| aag_concepts (概念) | 503 | verified 76.5% / passed 100% | 100% |
| aag_algorithms | 25 | — | 100% |
| aag_formulas | 41 | — | 100% |
| aag_metrics | 30 | — | 100% |
| aag_color_palettes | 40 | WCAG実測 | 100% |
| aag_typography_pairings | 30 | ライセンス記録 | 100% |
| aag_ui_patterns | 40 | — | 100% |
| aag_cases | 20 | 公開財務+S-1 | 100% |
| aag_heuristics | 50 | — | 100% |
| **合計** | **779** | **100% PASS** | **100%** |

## 16 サブフィールド分布

| SF | サブフィールド | 概念数 |
|----|--------------|--------|
| 01 | growth_acquisition | 50 |
| 02 | retention_engagement | 40 |
| 03 | ux_research | 40 |
| 04 | visual_design | 40 |
| 05 | gamification | 27 |
| 06 | behavioral_economics | 25 |
| 07 | network_effects | 23 |
| 08 | recommendation_algorithm | 26 |
| 09 | monetization_pricing | 37 |
| 10 | onboarding_activation | 28 |
| 11 | community_belonging | 24 |
| 12 | analytics_experimentation | 26 |
| 13 | brand_narrative | 32 |
| 14 | accessibility_inclusion | 30 |
| 15 | mobile_specific_ux | 26 |
| 16 | ai_generative_ux | 29 |

## 多様性指標 (Phase 11 で要補正)

| 指標 | 現状 | 目標 |
|------|------|------|
| Non-Western 率 | 13.5% | ≥20% |
| 女性研究者率 | 9.7% | ≥15% |
| Source URL | 100% | 100% ✓ |
| Verified | 76.5% | ≥95% |
| 多言語 | (測定保留) | ≥30% |

## 実行体制

- /adb v1.1 主指揮
- 6 並列 db-concept-builder (Wave A/B/C/D + 特殊テーブル + 算法/数式)
- 各エージェント 10件毎の seed JSON バッチ保存 (usage limit 対策)
- INSERT OR IGNORE 冪等ロード
- ハルシネーション検出 0 / 重複 0 / 合成URL 0

## 収録された主な非西洋概念
WeChat Mini Programs / Pinduoduo / Gojek Super App / KaiOS / M-Pesa / Nüshu (女书) /
KJ法 (川喜田二郎) / 場 (清水博) / 経営理念 (松下幸之助/稲盛和夫) / 和ブランド (原研哉) /
甘え (土居健郎) / 間 / 杉浦康平 / Ubuntu / 国潮 (Guochao) / Ikigai / Islamic 幾何 /
Kente / JIS X 8341-3 / GB/T 37668 / India GIGW / りんな / LINE CLOVA / 百度 ERNIE /
Bhashini / Arabic RTL AI / ハングル タイポグラフィ / Indigenous Storytelling / etc.

## 収録された主な女性研究者
Carol S. Pearson (Brand Archetype) / Melanie Green (Narrative Transportation) /
Jennifer Aaker (Brand Personality) / Kat Holmes (Inclusive Design Mismatch) /
Frances Berriman (PWA) / Erika Hall (Conversational Design) / Saleema Amershi (CHI 2019) /
Susan Athey (Causal Forests) / Jean Lave (CoP) / Kerry Rodden + Hilary Hutchinson (HEART) /
Marilyn Strathern (Goodhart 関連批評) / Edith Harbaugh (Feature Flagging) /
Bluma Zeigarnik / Karen Holtzblatt / Lucy Suchman / Batya Friedman / Shaowen Bardzell /
Jane Fulton Suri / Teresa Amabile / Barbara Fredrickson / Indrani Medhi / Susan Kare (Mac icons) /
Judy Brewer (WCAG/W3C WAI) / Liz Reid (AI Overviews) / Carrie Cai (AI Onboarding) /
Corinna Cortes (Smart Compose) / Simone Ahuja (Jugaad)

## 残作業 (次フェーズ)

- Phase 3 Validate: PASS 確認済
- Phase 4 Relations: 系譜 (predecessor/successor) を seed JSON で作成
- Phase 5 Dashboard: 赤白CI textbook style HTML 生成済 (~/projects/apps/miratuku-news-v2/dashboards/aag-db.html)
- Phase 7 Publish: /aag agent + command 作成済 (AR-DB hook 経由で自動同期)
- Phase 8 Audit: ak-quality-auditor で独立検証
- Phase 10 Codex 並列: 非西洋・女性比率の補正 (docs/phase10_codex_plan.md 参照)
- Phase 11 Iteration: 4 周まで反復
- Phase 13 IRR Gwet AC1 測定 (5件セット標準)
- Phase 14 18 DB cross_ref 紐付け (innovation/startup/mg/ss/dsd/ec/philosophy/anthropology/great-figures 等)
- Phase 15 Negative space 探索

## Dashboard

公開: `https://yuyanishimura0312.github.io/miratuku-news-v2/dashboards/aag-db.html`
ローカル: `~/projects/research/aag-db/dashboard/aag-db.html`

## Agent / Command

- `~/.claude/agents/aag.md` 作成済
- `~/.claude/commands/aag.md` 作成済
- AR-DB 自動同期 hook 経由で次回 ETL 時に登録される
