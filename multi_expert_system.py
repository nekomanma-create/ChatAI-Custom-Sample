#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Expert System
A collaborative system with multiple experts providing different approaches to tasks.
"""


class Planner:
    """
    基本的にプランナーです。タスクを整理し、適切なエキスパートを選択します。
    (Basically a planner. Organizes tasks and selects appropriate experts.)
    """
    
    def __init__(self):
        self.name = "Planner"
        self.experts = {}
    
    def register_expert(self, expert):
        """エキスパートを登録"""
        self.experts[expert.name] = expert
    
    def plan(self, task):
        """タスクに基づいてプランを作成"""
        return f"[{self.name}] タスクを分析しています: {task}"
    
    def delegate(self, task):
        """タスクを各エキスパートに委譲し、結果を収集"""
        results = []
        results.append(self.plan(task))
        
        # 各エキスパートに順番に対応させる
        for expert_name in ["Roger", "Lewis", "Sam", "Daniel"]:
            if expert_name in self.experts:
                expert = self.experts[expert_name]
                results.append(expert.respond(task))
        
        return "\n\n".join(results)


class Roger:
    """
    メンバー１．ロジャー：頼れるエンジニアリーダー。ソースコードをすぐに出してくれます。
    (Member 1. Roger: Reliable engineering leader. Immediately provides source code.)
    """
    
    def __init__(self):
        self.name = "Roger"
        self.role = "Engineering Leader"
    
    def respond(self, task):
        """タスクに対してソースコードを提供"""
        code_example = self._generate_code(task)
        return f"[{self.name} - {self.role}]\nソースコードを提供します:\n\n```python\n{code_example}\n```"
    
    def _generate_code(self, task):
        """タスクに応じたサンプルコードを生成"""
        return f"""# Solution for: {task}

def solve_task():
    '''
    タスクを解決するための実装
    '''
    result = process_task()
    return result

def process_task():
    # タスク処理のロジック
    return "Task completed successfully"

if __name__ == "__main__":
    result = solve_task()
    print(result)"""


class Lewis:
    """
    メンバー２．ルイス：冷静なサブリーダー。そのソースコードの解説をしてくれます。
    (Member 2. Lewis: Calm sub-leader. Explains the source code.)
    """
    
    def __init__(self):
        self.name = "Lewis"
        self.role = "Sub-Leader / Code Explainer"
    
    def respond(self, task):
        """コードの解説を提供"""
        explanation = self._explain_code(task)
        return f"[{self.name} - {self.role}]\nコードの解説:\n\n{explanation}"
    
    def _explain_code(self, task):
        """コードの詳細な解説"""
        return f"""このソリューションについて説明します:

1. **関数構造**: 
   - `solve_task()`: メイン関数として、タスクの解決フローを管理します
   - `process_task()`: 実際の処理ロジックを担当します

2. **設計の考え方**:
   - 関数を分離することで、テストと保守が容易になります
   - 各関数は単一責任の原則に従っています

3. **実行フロー**:
   - プログラムが実行されると、solve_task()が呼び出されます
   - 内部でprocess_task()を使用してタスクを処理します
   - 結果を返して表示します

このアプローチにより、拡張性と可読性が向上します。"""


class Sam:
    """
    メンバー３．サム：彼はマネージャーだ。そのプランの目的を一緒に考えることをしてくれる。
    (Member 3. Sam: He is a manager. Helps think about the purpose of the plan together.)
    """
    
    def __init__(self):
        self.name = "Sam"
        self.role = "Manager"
    
    def respond(self, task):
        """プランの目的について考察"""
        purpose_analysis = self._analyze_purpose(task)
        return f"[{self.name} - {self.role}]\nプランの目的について考えましょう:\n\n{purpose_analysis}"
    
    def _analyze_purpose(self, task):
        """プランの目的を分析"""
        return f"""このタスク「{task}」の目的を整理します:

**ビジネス価値**:
- ユーザーのニーズに応える解決策を提供
- 効率的な実装による時間とコストの削減
- 長期的な保守性の確保

**技術的目標**:
- クリーンで理解しやすいコード
- 拡張可能なアーキテクチャ
- テスト可能な設計

**成功基準**:
- 機能要件が満たされている
- コードの品質基準をクリア
- チーム全体が理解できる実装

これらの目的を念頭に置いて、最適なソリューションを目指しましょう。"""


class Daniel:
    """
    メンバー４．ダニエル：のんびり屋だ。彼はマイペースに最後に要点をズバリと過剰書きで書いてくれる。
    (Member 4. Daniel: Laid-back. He writes the key points clearly at the end in an excessive manner at his own pace.)
    """
    
    def __init__(self):
        self.name = "Daniel"
        self.role = "Summarizer"
    
    def respond(self, task):
        """要点を過剰書きでまとめる"""
        summary = self._create_summary(task)
        return f"[{self.name} - {self.role}]\nまぁまぁ、落ち着いて。要点をまとめるとこうだよ:\n\n{summary}"
    
    def _create_summary(self, task):
        """詳細な要点まとめ"""
        return f"""■■■ 要点まとめ ■■■

【タスク】: {task}

【結論】:
みんなの話をまとめるとね、こういうことだよ。

◆ Rogerが提供したコード
  → 実装の具体例を示してくれた
  → すぐに使える形でソースコードを提供
  → エンジニアリングの視点から最適解を出している

◆ Lewisの解説
  → コードの仕組みを丁寧に説明
  → なぜそうなっているのか理由も明確
  → 技術的な理解を深めるのに役立つ

◆ Samの目的分析
  → ビジネス的な価値を整理
  → なぜこのタスクをやるのか目的を明確化
  → 成功基準を定義して方向性を示す

【まとめのまとめ】:
つまりね、技術（Roger + Lewis）とビジネス（Sam）の両面から
しっかりアプローチできてるってこと。
これで完璧に要件を満たせるよ！

以上、のんびりだけど、ちゃんとまとめたよ～ 🎯"""


def create_multi_expert_system():
    """マルチエキスパートシステムを構築"""
    planner = Planner()
    
    # エキスパートを登録
    planner.register_expert(Roger())
    planner.register_expert(Lewis())
    planner.register_expert(Sam())
    planner.register_expert(Daniel())
    
    return planner


def main():
    """メイン実行関数"""
    print("=" * 80)
    print("マルチエキスパートシステム")
    print("Multi-Expert Collaborative System")
    print("=" * 80)
    print()
    
    # システムを構築
    system = create_multi_expert_system()
    
    # サンプルタスク
    task = "データ処理パイプラインの実装"
    
    print(f"📋 タスク: {task}")
    print()
    print("-" * 80)
    print()
    
    # タスクを委譲して結果を取得
    results = system.delegate(task)
    print(results)
    
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
