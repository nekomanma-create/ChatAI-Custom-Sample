#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Expert System - Usage Examples
さまざまなタスクでマルチエキスパートシステムを使用する例
"""

from multi_expert_system import create_multi_expert_system


def example1():
    """Example 1: Web APIの開発"""
    print("\n" + "=" * 80)
    print("例１: Web APIの開発タスク")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "RESTful APIエンドポイントの実装"
    
    results = system.delegate(task)
    print(results)


def example2():
    """Example 2: データベース設計"""
    print("\n" + "=" * 80)
    print("例２: データベース設計タスク")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "ユーザー管理システムのデータベーススキーマ設計"
    
    results = system.delegate(task)
    print(results)


def example3():
    """Example 3: パフォーマンス最適化"""
    print("\n" + "=" * 80)
    print("例３: パフォーマンス最適化タスク")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "大量データ処理のパフォーマンス改善"
    
    results = system.delegate(task)
    print(results)


def interactive_mode():
    """インタラクティブモード: カスタムタスクを入力"""
    print("\n" + "=" * 80)
    print("インタラクティブモード")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    
    print("マルチエキスパートシステムへようこそ！")
    print("解決したいタスクを入力してください (終了するには 'quit' を入力):\n")
    
    while True:
        task = input("タスク > ").strip()
        
        if task.lower() in ['quit', 'exit', 'q']:
            print("\nシステムを終了します。ありがとうございました！")
            break
        
        if not task:
            print("タスクを入力してください。\n")
            continue
        
        print("\n" + "-" * 80 + "\n")
        results = system.delegate(task)
        print(results)
        print("\n" + "-" * 80 + "\n")


if __name__ == "__main__":
    # 事前定義された例を実行
    print("マルチエキスパートシステム - 使用例")
    print("Multi-Expert System - Usage Examples")
    
    choice = input("\n実行モードを選択してください:\n1. 例１: Web API開発\n2. 例２: データベース設計\n3. 例３: パフォーマンス最適化\n4. インタラクティブモード\n選択 (1-4): ").strip()
    
    if choice == "1":
        example1()
    elif choice == "2":
        example2()
    elif choice == "3":
        example3()
    elif choice == "4":
        interactive_mode()
    else:
        print("\n全ての例を実行します...\n")
        example1()
        example2()
        example3()
