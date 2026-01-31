# Quick Reference Guide / クイックリファレンスガイド

## マルチエキスパートシステム (Multi-Expert System)

### メンバー構成 (Team Structure)

| 名前 | 役割 | 特徴 |
|------|------|------|
| **Planner** | タスク整理 | タスクを分析し、エキスパートに委譲する |
| **Roger** | Engineering Leader | ソースコードをすぐに提供 |
| **Lewis** | Sub-Leader | コードの詳細な解説を提供 |
| **Sam** | Manager | プランの目的とビジネス価値を分析 |
| **Daniel** | Summarizer | 要点をわかりやすくまとめる |

### 使用方法 (Usage)

#### 1. 基本的な実行 (Basic Execution)
```bash
python multi_expert_system.py
```

#### 2. 使用例の実行 (Run Examples)
```bash
python example_usage.py
```

#### 3. 追加シナリオ (Additional Scenarios)
```bash
python additional_scenarios.py
```

#### 4. テストの実行 (Run Tests)
```bash
python -m unittest test_multi_expert_system.py -v
```

### プログラムでの使用 (Programmatic Usage)

```python
from multi_expert_system import create_multi_expert_system

# システムを作成
system = create_multi_expert_system()

# タスクを実行
task = "あなたのタスクをここに記述"
results = system.delegate(task)

# 結果を表示
print(results)
```

### 各エキスパートの応答例 (Expert Response Examples)

#### Roger の応答
- ✅ 実装可能なソースコード
- ✅ すぐに使える形式
- ✅ ベストプラクティスに基づく設計

#### Lewis の応答
- ✅ コードの構造説明
- ✅ 設計の考え方
- ✅ 実行フローの解説

#### Sam の応答
- ✅ ビジネス価値の分析
- ✅ 技術的目標の整理
- ✅ 成功基準の定義

#### Daniel の応答
- ✅ 全体の要点まとめ
- ✅ わかりやすい構造
- ✅ 親しみやすい表現

### ファイル構成 (File Structure)

```
ChatAI-Custom-Sample/
├── .gitignore                    # Git除外設定
├── README.md                     # プロジェクト説明
├── QUICK_REFERENCE.md           # このファイル
├── multi_expert_system.py       # メインシステム
├── example_usage.py             # 使用例
├── additional_scenarios.py      # 追加シナリオ
└── test_multi_expert_system.py  # テストスイート
```

### シナリオ例 (Example Scenarios)

1. **Web API開発** - RESTful APIの実装
2. **データベース設計** - スキーマ設計
3. **パフォーマンス最適化** - 処理速度の改善
4. **機械学習** - モデルの実装
5. **セキュリティ** - 認証・認可の強化
6. **マイクロサービス** - アーキテクチャ設計
7. **テスト自動化** - CI/CDパイプライン
8. **データパイプライン** - リアルタイム処理
9. **モバイルアプリ** - クロスプラットフォーム開発

### テストカバレッジ (Test Coverage)

- ✅ Planner: 5 tests
- ✅ Roger: 3 tests
- ✅ Lewis: 3 tests
- ✅ Sam: 3 tests
- ✅ Daniel: 3 tests
- ✅ Integration: 3 tests
- **合計: 20 tests (全て合格)**

### トラブルシューティング (Troubleshooting)

#### Q: Python バージョンは？
A: Python 3.6以上が必要です

#### Q: 依存関係は？
A: 標準ライブラリのみを使用しています

#### Q: カスタムタスクの実行方法は？
A: `example_usage.py`のインタラクティブモード（選択肢4）を使用してください

#### Q: エキスパートの順序を変更できますか？
A: `Planner.delegate()`メソッドでエキスパートの順序をカスタマイズできます

---

## Security Summary / セキュリティサマリー

✅ **CodeQL スキャン**: 0件の脆弱性  
✅ **依存関係**: 外部依存なし（標準ライブラリのみ）  
✅ **コードレビュー**: 完了、全てのフィードバックに対応済み
