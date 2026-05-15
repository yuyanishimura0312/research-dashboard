---
title: HTP-DB 構築レポート — 人類が生成した文字・テキストの 5,226 年
date: 2026-05-16
type: research-database-construction
status: published
github: https://github.com/yuyanishimura0312/htp-db
dashboard: https://yuyanishimura0312.github.io/htp-db/
report: https://yuyanishimura0312.github.io/htp-db/report.html
agent: /htp
keywords: [HTP-DB, Human Text Production, 情報生産2030-2100, AI生成テキスト, Buringh, IDC, Epoch AI, 動詞転換, path-1, db-master]
---

# HTP-DB 構築レポート — 人類が生成した文字・テキストの 5,226 年

**Human Text Production Database** — Wave 1-4 完走報告書

## 公開リソース

- **GitHub Pages ダッシュボード**: https://yuyanishimura0312/htp-db.github.io/ （ライブビュー、補論+図解6点）
- **包括レポート HTML**: https://yuyanishimura0312.github.io/htp-db/report.html （約19K字、12章）
- **GitHub リポジトリ**: https://github.com/yuyanishimura0312/htp-db （public）
- **専属エージェント**: `/htp` (Claude Code)
- **SQLite DB**: `~/projects/research/htp-db/htp.db`

## 構築指標

| 項目 | 値 |
|---|---|
| 期間カバー | BC3200 〜 AD2026 / 5,226年 |
| Records | 47 (unified_volume) |
| Sources | 23 (authority_tier 1: 14 / 2-3: 9) |
| Cross-refs | 15 (既存64DB + CLA/FVCP/Megatrend他) |
| Discrepancies | 5 (含: AI 2025 API vs unique 150x gap) |
| Media types | 12 (楔形文字 → AI生成テキスト) |
| Language regions | 9 圏 (8充足 + 1部分) |
| source_url_live_rate | 100% (23/23) |
| verified_rate | 59.1% (Wave 1-2 のみ 80.6%) |
| FDD | 累積 2 FDD (Wave 1-4 同日完走) |

## 着手から完成までの流れ

2026-05-15 着手、2026-05-16 レポート公開。/db-master Tier 0 メタオーケストレーター経由で 5 段階方法論（BlindSpot → Verify → Design → Integrate → AutoBuild）を完走し、Wave 1（1450-2026）、Wave 2（500-1450）、Wave 3（BC3200-AD500）、Wave 4（言語圏拡張+AI時代）を同日に達成した。

## 設計の核 — 三つの原則

### path-1 真実層
Buringh / IDC / UNESCO を期間別に authority_tier 層別固定。差分は `htp_source_discrepancies` で透明化。結論を一つに収束させない。

### v2 失敗継承
過去 text-corpus 系DB（PESTLE / CI / Myth）の三大失敗（推定/実測混在・言語圏不均衡・媒体定義揺れ）を構造レベルで再発防止。`gta_status` 4値 / `coverage_flag` / `medium_definition` 固定で実装。

### 件数禁止 KPI
verified_rate / source_url_live_rate / cross_refs / estimation_traceability の四本柱。「N万件」を成果指標にしない。

## 主要発見

### 5 つの転換点
1. BC3200 楔形文字発明 — テキストはまず行政のための技術として始まった
2. 9世紀カロリング・ルネサンス — 写本生産が2.5K→91K（3.6倍）
3. 12世紀ルネサンス — 写本生産が134K→768K（5.7倍急増）
4. 1454 グーテンベルク活版 — 46年で1,250万部、その後14桁の爆発
5. 2022 ChatGPT 公開 — 新しい動詞「共に生成する」の境界

### 2025 AI交差点の限定的妥当性
当初 seed の「1-20京 tokens」は **API消費量と実生成量を取り違えると意味が反転**する数値であった。Wave 4.5 で三層分離：

- **API 消費量**: 1.5×10¹⁷ tokens/年（OpenAI + 全プロバイダー、verified）
- **新規生成 unique テキスト**: 1.0×10¹⁵ tokens/年（Epoch AI 推算、信頼度LOW-MED）
- **累積人類テキスト総量**: 3.0×10¹⁴ tokens（Epoch AI 2024 baseline）

層間ギャップ 150 倍。「人類超過 2025」は文脈依存：
- 新規Web記事フロー: AI 52% / 人間 48%（Graphite 2025-05, n=65K）— **超過済**
- 累積ストック: AI 15% / 人間 85% — **未超過**

### 欧米中心からの脱却
Wave 1 で 5/9 圏 → Wave 4 で 8/9 圏カバー。決定的だったのは Shamela（peer-reviewed 1B語アラビア語）と Sinica（700M字漢字）の組み込み。

## ミラツク事業への含意

1. **翻訳的編集の価値上昇** — Web記事の半分がAI生成 → 一次解釈の希少性が逆に高まる（連載「〜のかたち」/ esse-sense 記事）
2. **累積知の信頼基盤** — 学術 DB 群の引用検証・source_url 100% が機能不可欠インフラへ
3. **探究の協働的拡張** — codex-team / FVCP で人類1人の1,000倍速の探究
4. **混入リスクへの反証 DB 必須化** — human-verified flag が次の品質ゲート

## 補論「情報生産の2030-2100」への接続

HTP-DB は、未だ未執筆の deep knowledge 補論「情報生産の2030-2100」の歴史根拠層として機能する。動詞転換 4 段階「書き写す → 印刷する → 発信する → 共に生成する」を量データで裏打ち。/future-vision-orchestrate（FVCP）起動で 4-6 週間で初版執筆可能。

## Wave 5-7 ロードマップ

- Wave 5: 古代誤差幅縮小・深化
- Wave 6: 「情報生産の2030-2100」FVCP双方向統合
- Wave 7: UNESCO 個別国別データ・図書館蔵書統計の細粒度化

## メタ知見 — DB構築方法論の実証

本構築は、ミラツクのプロセスメタ原則 5 箇条と暗黙知 7 パターンを構造的に体現した実例である。生成と検証の分離、DB完成後成果物、件数→検証通過率、削除よりフラグ、Wave段階展開、メタデータ多軸化、訂正版の重ね方の七つが、それぞれ DDL の特定箇所に対応する。

特筆すべきは「path-1 真実層」の運用実証：Wave 4.5 で「1-20京tokens」の意味が層によって反転することが判明した際、当初 seed を削除せず、新規レコードで層別分離し、`htp_source_discrepancies` に gap_ratio=150 を記録することで、訂正版を重ねる誠実性を実装した。これは LP正規化作業（7+1の問い）で実証された原則の汎用化である。

## 引用構造

外部 cross-ref 15 件：TA / CDH / CI / SI / MG / PESTLE / UPR / TK / GC-DB / FTT-DB v2 / CLA / SI-Framework / Megatrend / FVCP / Manufacturing-Orchestra

これらは HTP-DB を生態系の一部として機能させるための統一参照テーブル `htp_cross_db_refs` に格納。新規DBが単独で完成するのではなく、既存64DBの中に組み込まれる設計を体現する。

## 学術検証

- 全 source_url（23本）2026-05-15 に live 確認済
- ハルシネーション疑い 2 件を識別して採用保留（Bibliotheca Alexandrina「100K manuscripts」目標未達成不明、NDL「江戸期1,400万件」根拠未確認）
- AI 2025 推定値は独立 researcher エージェントで再検証、Epoch AI / OpenAI / Graphite で交叉照合

## 公開後の運用

`/htp` エージェントで照会可能。GitHub Pages により外部からダッシュボード・レポートの閲覧が即時可能。デプロイ後の更新は git push でそのまま反映。

---

**著者**: 西村勇也（NPO法人ミラツク）+ Claude Opus 4.7（1M context）
**作成**: 2026-05-15 着手 / 2026-05-16 レポート公開
**経路**: /db-master Tier 0 → 経路B 実データDB → Wave 1-4 同日完走
