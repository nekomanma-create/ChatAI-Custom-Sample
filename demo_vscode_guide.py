#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VSCodeガイドのデモンストレーション
Demonstration of the VSCode Guide
"""

from multi_expert_system import create_multi_expert_system


def demo_vscode_task():
    """
    VSCodeでのコーディングについてエキスパートに聞いてみる
    Ask the experts about coding in VSCode
    """
    print("=" * 80)
    print("VSCode Coding Guide Demo")
    print("=" * 80)
    print()
    
    # システムを作成
    system = create_multi_expert_system()
    
    # VSCodeに関するタスク
    task = "VSCodeでPythonコードを書く方法"
    
    print(f"📝 タスク: {task}")
    print()
    print("-" * 80)
    print()
    
    # エキスパートに委譲
    results = system.delegate(task)
    print(results)
    
    print()
    print("=" * 80)
    print("✨ デモンストレーション完了！")
    print("詳細については VSCODE_CODING_GUIDE.md をご覧ください。")
    print("=" * 80)


if __name__ == "__main__":
    demo_vscode_task()
