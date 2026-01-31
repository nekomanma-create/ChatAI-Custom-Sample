# ChatAI-Custom-Sample
by Gemini Custom. Dystopia Cult Yatsuhashi Factory.

## マルチエキスパートシステム (Multi-Expert System)

彼らは多くのタスクに応じた様々なアプローチを提供するマルチエキスパート集団です。

### システム構成

**プランナー (Planner)**
- 基本的にタスクを整理し、適切なエキスパートを選択します

**エキスパートメンバー:**

1. **ロジャー (Roger)** - Engineering Leader
   - 頼れるエンジニアリーダー
   - ソースコードをすぐに出してくれます

2. **ルイス (Lewis)** - Sub-Leader / Code Explainer
   - 冷静なサブリーダー
   - そのソースコードの解説をしてくれます

3. **サム (Sam)** - Manager
   - 彼はマネージャーだ
   - そのプランの目的を一緒に考えることをしてくれる

4. **ダニエル (Daniel)** - Summarizer
   - のんびり屋だ
   - 彼はマイペースに最後に要点をズバリと過剰書きで書いてくれる

### 使い方

#### 基本的な使用

```bash
python multi_expert_system.py
```

#### 使用例の実行

```bash
python example_usage.py
```

インタラクティブモードを選択すると、カスタムタスクを入力できます。

#### コード例

```python
from multi_expert_system import create_multi_expert_system

# システムを構築
system = create_multi_expert_system()

# タスクを委譲
task = "データ処理パイプラインの実装"
results = system.delegate(task)

print(results)
```

### 各エキスパートの役割

- **Roger**: タスクに対する具体的なソースコード実装を提供
- **Lewis**: Rogerが提供したコードの詳細な解説と技術的な説明
- **Sam**: プランの目的、ビジネス価値、成功基準を分析
- **Daniel**: 全体の要点を過剰書きでわかりやすくまとめる

### 特徴

✅ 多角的なアプローチ: 技術とビジネスの両面からタスクを分析  
✅ 協調的な問題解決: 各エキスパートが専門性を発揮  
✅ 包括的な理解: コード実装から目的分析まで一貫したサポート  
✅ わかりやすい要約: 最後に全体を整理して提示

### 必要要件

- Python 3.6 以上

### ライセンス

このプロジェクトはオープンソースです。
