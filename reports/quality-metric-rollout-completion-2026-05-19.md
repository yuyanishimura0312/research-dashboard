# 品質指標 5 件セット標準 — DB 全体ロールアウト完了報告

**実行日**: 2026-05-19
**対象**: ミラツク/esse-sense エコシステム全 DB（174 DB / 185 ファイル）
**根拠**: `~/.claude/rules/quality-metrics-standard.md`（Cohen のカッパ係数方法論検証の結果）
**ツール**: `/tmp/rollout_quality_status.py` + `~/projects/research/agent-registry-db/tools/gwet_ac1.py`

---

## 1. ロールアウト結果

| ステータス | DB 数 | 意味 |
|---|---|---|
| `kappa_only_legacy_2026_05_19` | **7** | κ 公表済。5 件セットへ再測定要 |
| `no_irr_measurement_2026_05_19` | **50** | IRR 未測定。新規測定時は 5 件セット必須 |
| 要スキーマ追加（_quality_metadata なし） | 43 | 後日スキーマ追加が必要 |
| 小規模スキップ（< 100 KB） | 56 | snapshots / 補助 DB 等 |
| エラー | **0** | 全 4 スキーマ変種に対応完了 |

**処理成功率**: スキーマ対応 DB 100 件中 57 件にステータス記録完了（57%）。残り 43 件はスキーマ追加後にマーク予定。

## 2. κ 公表済 7 DB（最優先で 5 件セット再測定対象）

検証の結果、当初認識していた 5 DB に加え、新たに 2 DB が κ 公表していたことが判明：

| DB | 既存 κ 値 | 注意 |
|---|---|---|
| **physics-concepts-db** | 0.5006 〜 0.8745（v1-v6） | 物理基盤、被参照頻度高 |
| **cosmic-earth-history-db** | broad 0.0768 / canonical 0.9863 | パラドックス兆候顕著 |
| **earth-science-db** | broad 0.7325 / canonical 0.9317 | カテゴリ粒度依存 |
| **botany-concepts-db** | 0.8602（broad） | ほぼ完全 |
| **time-concepts-db** | 0.97（推定） | スキーマ別形式 |
| **chemistry-concepts-db** | （要確認） | **新規発見** |
| **great_figures（research）** | （要確認） | **新規発見** |

## 3. スキーマ別対応実績

ロールアウトで遭遇した `_quality_metadata` テーブルのスキーマ変種：

| スキーマ | キー列 | 値列 | タイムスタンプ列 | 件数 |
|---|---|---|---|---|
| v1 | metric | value | measured_at | 多数 |
| v2 | metric_key | metric_value | updated_at | 一部（metric_type+description 含む特殊形式） |
| v3 | key | value | last_updated | 約 10 件 |
| v4 | metric_name | metric_value | measured_at | 1 件（dkf） |
| v5 | key | value | measured_at | 2 件（toi-no-sairai） |
| v6 | key | value | updated_at | 1 件（ss-db） |

スクリプト側で 4 種の候補キー列 × 2 種の候補値列 × 3 種の候補タイムスタンプ列を動的判定する設計に統一し、エラー 0 を達成。

## 4. _quality_metadata テーブルがない 43 DB

以下のグループは後日スキーマ追加が必要：

- 大規模実データ DB: contemporary_questions / dissertation_genealogy / ftt / fvcp-meta / industry-academic-corporate-needs / investment-signal / pestle-news / policy / sgrd / cdh / academic_landscape 等
- 小規模ユーティリティ DB: foresight-verification / human-activities / apk / qol_sensibility 等

これらは Wave 2 で `_quality_metadata` テーブル追加 + ステータス記録のセットで対応する。

## 5. 次の運用ステップ

### 即時運用変更（本日より発効）

- 新規 DB 構築時は `_quality_metadata` テーブルを必ず作成
- 評価者間一致度の測定は **5 件セット必須**（カッパ単独公表禁止）
- 主指標は Gwet's AC1（κ は参考値）

### 計画的タスク（順次実行）

1. **7 DB の 5 件セット再測定**（最優先）
   - 生評価データの再収集
   - `gwet_ac1.py` で 5 指標を一括算出
   - `_quality_metadata` に新ステータス `5set_complete_<date>` を記録
2. **43 DB へのスキーマ追加**（Wave 2、約 5 FDD）
   - `_quality_metadata` テーブル作成
   - 該当ステータスを記録
3. **公開ダッシュボード更新**
   - AR-DB ダッシュボードに「品質メトリクス状態」列追加
   - 各 DB の状態を可視化

## 6. アイデンティティへの寄与

「学術知の ConceptNet」アイデンティティの **品質保証軸** について、本ロールアウトで以下が確立された：

- エコシステム全体に **統一品質指標方針**（5 件セット）が記録された（57 DB）
- 既存 κ 公表値の **方法論的限界が明示**された（7 DB の legacy 状態）
- 今後の新規測定は **2020 年代の学術基準**（Gwet AC1 主指標）に準拠
- 残作業（43 DB のスキーマ追加）が **明確な工数見積で可視化**された

ConceptNet が 27 年間踏み込まなかった「DB 単位の評価者間信頼性公表」領域を、本エコシステムは方法論的限界の自覚を伴って強化する立場にある。

---

## 実行コマンド履歴

```bash
# 1. ロールアウト実行（スキーマ 4 種対応）
python3 /tmp/rollout_quality_status.py

# 2. 結果検証
python3 -c "...status_counts..."  # 上記サマリ取得

# 3. Gwet AC1 計算ツール self-test
python3 ~/projects/research/agent-registry-db/tools/gwet_ac1.py --self-test
```

## 関連ファイル

- ルール正本: `~/.claude/rules/quality-metrics-standard.md`
- 計算ツール: `~/projects/research/agent-registry-db/tools/gwet_ac1.py`
- メモリ: `~/.claude/projects/-Users-nishimura-/memory/feedback_quality_metrics_5set.md`
- ロールアウトスクリプト: `/tmp/rollout_quality_status.py`
- 詳細 JSON: `/tmp/rollout_quality_status_result.json`
- 先行レポート: `reports/ar-db-self-improvement-proposals-2026-05-19.md`
- アイデンティティ典拠: `dashboards/academic-conceptnet-hypothesis.html`
