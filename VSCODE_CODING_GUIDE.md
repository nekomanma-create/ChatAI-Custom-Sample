# VSCode でコードを書く方法 / How to Write Code in VSCode

このガイドでは、Visual Studio Code（VSCode）を使用してコードを書く方法を解説します。

## 目次 (Table of Contents)

1. [VSCodeのインストール](#vscodeのインストール)
2. [基本的な使い方](#基本的な使い方)
3. [Python開発の環境構築](#python開発の環境構築)
4. [推奨拡張機能](#推奨拡張機能)
5. [コードの作成と編集](#コードの作成と編集)
6. [デバッグ方法](#デバッグ方法)
7. [ターミナルの使用](#ターミナルの使用)
8. [便利なショートカット](#便利なショートカット)
9. [このプロジェクトでの実践例](#このプロジェクトでの実践例)

---

## VSCodeのインストール

### 1. ダウンロード
1. [VSCode公式サイト](https://code.visualstudio.com/)にアクセス
2. お使いのOS（Windows/Mac/Linux）に対応したバージョンをダウンロード
3. インストーラーを実行してインストール

### 2. 初回起動
```
VSCode を起動すると、ウェルカム画面が表示されます。
ここから新しいファイルを作成したり、フォルダを開いたりできます。
```

---

## 基本的な使い方

### プロジェクトフォルダを開く

**方法1: メニューから**
```
File（ファイル）→ Open Folder（フォルダを開く）
→ プロジェクトフォルダを選択
```

**方法2: コマンドライン**
```bash
# プロジェクトフォルダに移動
cd /path/to/your/project

# VSCodeで開く
code .
```

### ファイルの作成

1. **エクスプローラーパネル**（左側のサイドバー）を使用
2. フォルダアイコンの横にある **「新しいファイル」** アイコンをクリック
3. ファイル名を入力（例: `hello.py`）
4. Enterキーを押して確定

### ファイルの保存

- **保存**: `Ctrl+S` (Windows/Linux) または `Cmd+S` (Mac)
- **すべて保存**: `Ctrl+K S` (Windows/Linux) または `Cmd+K S` (Mac)

---

## Python開発の環境構築

### 1. Pythonのインストール確認

ターミナルで確認:
```bash
python --version
# または
python3 --version
```

### 2. Python拡張機能のインストール

1. VSCodeの左側のサイドバーから **拡張機能** アイコン（四角が4つのアイコン）をクリック
2. 検索ボックスに「Python」と入力
3. Microsoft公式の「Python」拡張機能をインストール

### 3. Pythonインタープリターの選択

1. `Ctrl+Shift+P` (Windows/Linux) または `Cmd+Shift+P` (Mac)でコマンドパレットを開く
2. 「Python: Select Interpreter」と入力
3. 使用するPythonバージョンを選択

---

## 推奨拡張機能

### Python開発に必須の拡張機能

| 拡張機能名 | 説明 | インストールコマンド |
|-----------|------|---------------------|
| **Python** | Pythonの基本サポート（IntelliSense、デバッグなど） | Microsoft公式 |
| **Pylance** | 高度なPython言語サーバー | 自動でPython拡張と一緒にインストール |
| **Python Indent** | Pythonのインデント自動調整 | おすすめ |
| **autoDocstring** | docstringの自動生成 | おすすめ |

### 一般的に便利な拡張機能

- **GitLens**: Git履歴の可視化
- **Prettier**: コードフォーマッター
- **Path Intellisense**: パスの自動補完
- **Bracket Pair Colorizer**: 括弧の色分け
- **Material Icon Theme**: ファイルアイコンテーマ

---

## コードの作成と編集

### 基本的なコードの書き方

#### 1. 新しいPythonファイルを作成

```python
# hello.py
def greet(name):
    """
    名前を受け取って挨拶を返す関数
    """
    return f"こんにちは、{name}さん！"

if __name__ == "__main__":
    message = greet("太郎")
    print(message)
```

#### 2. IntelliSense（コード補完）の使用

- 入力を始めると、自動的に候補が表示されます
- `Ctrl+Space`で強制的に候補を表示
- 矢印キーで選択、`Enter`で確定

#### 3. コードのフォーマット

- **ドキュメント全体**: `Shift+Alt+F` (Windows/Linux) または `Shift+Option+F` (Mac)
- **選択範囲のみ**: コードを選択して上記のショートカット

### コードスニペットの使用

よく使うコードパターンを素早く入力:

```python
# "def" と入力して Tab キーを押すと関数テンプレートが展開
def function_name(parameters):
    pass

# "class" と入力して Tab キーを押すとクラステンプレートが展開
class ClassName:
    def __init__(self):
        pass
```

---

## デバッグ方法

### 1. ブレークポイントの設定

- コード行の左側（行番号の左）をクリックして赤い点を表示
- ブレークポイント = プログラム実行を一時停止する位置

### 2. デバッグの開始

**方法1: デバッグパネルから**
1. 左側のサイドバーから **虫のアイコン**（デバッグとラン）をクリック
2. 「Run and Debug」ボタンをクリック
3. 「Python File」を選択

**方法2: ショートカット**
- `F5`キーを押す

### 3. デバッグ操作

デバッグ中に使用できるボタン:

- **Continue (F5)**: 次のブレークポイントまで実行
- **Step Over (F10)**: 1行ずつ実行（関数は飛ばす）
- **Step Into (F11)**: 関数の中に入る
- **Step Out (Shift+F11)**: 現在の関数から抜ける
- **Restart (Ctrl+Shift+F5)**: デバッグを再起動
- **Stop (Shift+F5)**: デバッグを停止

### 4. 変数の確認

- デバッグパネルの「Variables」セクションで変数の値を確認
- コード上で変数にマウスをホバーすると値が表示される
- 「Watch」セクションで特定の式を監視

---

## ターミナルの使用

### ターミナルを開く

- **メニュー**: Terminal → New Terminal
- **ショートカット**: `` Ctrl+` `` (バッククォート)

### Pythonコードの実行

```bash
# 単一ファイルの実行
python hello.py

# または
python3 hello.py

# このプロジェクトの例
python multi_expert_system.py
```

### 複数のターミナル

- ターミナルパネルの右上の「+」ボタンで新しいターミナルを追加
- ドロップダウンでターミナルを切り替え

---

## 便利なショートカット

### ファイル操作

| 操作 | Windows/Linux | Mac |
|------|--------------|-----|
| ファイルを開く | `Ctrl+O` | `Cmd+O` |
| ファイルを保存 | `Ctrl+S` | `Cmd+S` |
| 別名で保存 | `Ctrl+Shift+S` | `Cmd+Shift+S` |
| ファイルを閉じる | `Ctrl+W` | `Cmd+W` |
| クイックオープン | `Ctrl+P` | `Cmd+P` |

### 編集

| 操作 | Windows/Linux | Mac |
|------|--------------|-----|
| 行を複製 | `Shift+Alt+↓` | `Shift+Option+↓` |
| 行を削除 | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| 行を上下移動 | `Alt+↑/↓` | `Option+↑/↓` |
| コメントアウト | `Ctrl+/` | `Cmd+/` |
| 全選択 | `Ctrl+A` | `Cmd+A` |
| 元に戻す | `Ctrl+Z` | `Cmd+Z` |
| やり直し | `Ctrl+Y` | `Cmd+Shift+Z` |

### 検索と置換

| 操作 | Windows/Linux | Mac |
|------|--------------|-----|
| 検索 | `Ctrl+F` | `Cmd+F` |
| 置換 | `Ctrl+H` | `Cmd+H` |
| ファイル全体で検索 | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| 次を検索 | `F3` | `Cmd+G` |
| 前を検索 | `Shift+F3` | `Cmd+Shift+G` |

### 表示

| 操作 | Windows/Linux | Mac |
|------|--------------|-----|
| コマンドパレット | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| ターミナル表示/非表示 | `` Ctrl+` `` | `` Cmd+` `` |
| サイドバー表示/非表示 | `Ctrl+B` | `Cmd+B` |
| エクスプローラー | `Ctrl+Shift+E` | `Cmd+Shift+E` |
| 検索 | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| Git | `Ctrl+Shift+G` | `Cmd+Shift+G` |

### マルチカーソル

| 操作 | Windows/Linux | Mac |
|------|--------------|-----|
| カーソルを追加 | `Alt+Click` | `Option+Click` |
| 上にカーソル追加 | `Ctrl+Alt+↑` | `Cmd+Option+↑` |
| 下にカーソル追加 | `Ctrl+Alt+↓` | `Cmd+Option+↓` |
| 次の一致を選択 | `Ctrl+D` | `Cmd+D` |
| すべての一致を選択 | `Ctrl+Shift+L` | `Cmd+Shift+L` |

---

## このプロジェクトでの実践例

### ステップ1: プロジェクトを開く

```bash
# VSCodeでプロジェクトフォルダを開く
code /path/to/ChatAI-Custom-Sample
```

### ステップ2: メインファイルを確認

1. エクスプローラーで `multi_expert_system.py` をクリック
2. コードの構造を確認

### ステップ3: コードを実行

```bash
# ターミナルを開く（Ctrl+`）
# コードを実行
python multi_expert_system.py
```

### ステップ4: コードを編集

例: 新しいタスクを試す

```python
# multi_expert_system.py の main() 関数を編集
def main():
    system = create_multi_expert_system()
    
    # カスタムタスクに変更
    task = "VSCodeでPythonコードを書く方法"
    
    results = system.delegate(task)
    print(results)
```

### ステップ5: デバッグ

1. `multi_expert_system.py` の適当な行にブレークポイントを設定
2. `F5`でデバッグを開始
3. 変数の値を確認しながらステップ実行

### ステップ6: テストを実行

```bash
# ユニットテストを実行
python -m unittest test_multi_expert_system.py -v
```

---

## よくある質問 (FAQ)

### Q1: インデントエラーが出る
**A**: Pythonではインデントが重要です。VSCodeの設定でタブをスペースに変換するよう設定してください:
```json
{
    "editor.insertSpaces": true,
    "editor.tabSize": 4
}
```

### Q2: コード補完が効かない
**A**: 
1. Python拡張機能がインストールされているか確認
2. Pythonインタープリターが選択されているか確認（左下に表示）
3. VSCodeを再起動

### Q3: ターミナルでPythonが見つからない
**A**: 
1. Pythonが正しくインストールされているか確認
2. 環境変数PATHにPythonが含まれているか確認
3. VSCodeの設定でPythonパスを明示的に指定

### Q4: 日本語が文字化けする
**A**: ファイルのエンコーディングをUTF-8に設定:
- 右下のエンコーディング表示をクリック
- 「UTF-8で保存」を選択

---

## 設定のカスタマイズ

### settings.jsonの編集

`Ctrl+Shift+P` → 「Preferences: Open Settings (JSON)」

```json
{
    // エディタ設定
    "editor.fontSize": 14,
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "editor.minimap.enabled": true,
    
    // Python設定
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "autopep8",
    "python.analysis.typeCheckingMode": "basic",
    
    // ターミナル設定
    "terminal.integrated.fontSize": 13,
    "terminal.integrated.cursorBlinking": true,
    
    // ファイル設定
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "files.encoding": "utf8"
}
```

---

## まとめ

このガイドで学んだこと:

✅ VSCodeのインストールと基本操作  
✅ Python開発環境のセットアップ  
✅ コードの作成、編集、実行  
✅ デバッグの方法  
✅ 便利なショートカット  
✅ 実践的なワークフロー

### 次のステップ

1. **実際に手を動かす**: このプロジェクトのコードを編集してみる
2. **拡張機能を試す**: 便利な拡張機能を探してインストール
3. **ショートカットを覚える**: よく使う操作のショートカットを習得
4. **デバッグを活用**: ブレークポイントを使ってコードの動作を理解

---

## 参考リンク

- [VSCode公式ドキュメント（日本語）](https://code.visualstudio.com/docs?locale=ja)
- [Python in VSCode](https://code.visualstudio.com/docs/python/python-tutorial)
- [VSCode Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

---

**Happy Coding! 🎉**
