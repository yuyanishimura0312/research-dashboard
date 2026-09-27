# build-record

## 2026-09-27 保存と定期更新から有料APIの呼び出しを外す（既定で無効）
- 採った: `save-research.sh` と `update-digests.sh` の要約生成・AI分析を `ENABLE_PAID_DIGEST=1` のときだけ動かす。既定は無効。埋め込みの再生成（ローカルのモデル）は残す。西村さんに確認済み（「APIは使わずに実行してください」）。
- 棄却した: スクリプトの削除（戻せなくなる）／launchd の unload（定期の埋め込み更新まで止まる）。
- 実測: `/tmp/research-digests.log` に `'ThinkingBlock' object has no attribute 'text'` が 246 回。直近の実行は 1 回あたり 52〜55 件が失敗し、生成は 0〜1 件。応答を受け取ってから解析で落ちているので、呼び出し自体は成立していたとみられる（課金の有無は未確認）。
- 破綻条件: 2026-10-04 までに `/tmp/research-digests.log` に `ThinkingBlock` の新しい行が出たら、別の経路から呼ばれている。
- SCK: no matching rule
