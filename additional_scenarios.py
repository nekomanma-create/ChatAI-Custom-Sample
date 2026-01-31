#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Additional Example Scenarios for Multi-Expert System
追加のシナリオ例
"""

from multi_expert_system import create_multi_expert_system


def scenario_machine_learning():
    """シナリオ: 機械学習モデルの開発"""
    print("\n" + "=" * 80)
    print("シナリオ: 機械学習モデルの開発")
    print("Scenario: Machine Learning Model Development")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "画像分類のための畳み込みニューラルネットワークの実装"
    
    results = system.delegate(task)
    print(results)


def scenario_security():
    """シナリオ: セキュリティ対策の実装"""
    print("\n" + "=" * 80)
    print("シナリオ: セキュリティ対策の実装")
    print("Scenario: Security Implementation")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "認証・認可システムのセキュリティ強化"
    
    results = system.delegate(task)
    print(results)


def scenario_microservices():
    """シナリオ: マイクロサービスアーキテクチャの設計"""
    print("\n" + "=" * 80)
    print("シナリオ: マイクロサービスアーキテクチャの設計")
    print("Scenario: Microservices Architecture Design")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "Eコマースプラットフォームのマイクロサービス分割設計"
    
    results = system.delegate(task)
    print(results)


def scenario_testing():
    """シナリオ: テスト自動化の構築"""
    print("\n" + "=" * 80)
    print("シナリオ: テスト自動化の構築")
    print("Scenario: Test Automation Setup")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "CI/CDパイプラインでの自動テストフレームワーク構築"
    
    results = system.delegate(task)
    print(results)


def scenario_data_pipeline():
    """シナリオ: リアルタイムデータパイプラインの構築"""
    print("\n" + "=" * 80)
    print("シナリオ: リアルタイムデータパイプラインの構築")
    print("Scenario: Real-time Data Pipeline")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "ストリーミングデータのリアルタイム処理パイプライン実装"
    
    results = system.delegate(task)
    print(results)


def scenario_mobile_app():
    """シナリオ: モバイルアプリケーション開発"""
    print("\n" + "=" * 80)
    print("シナリオ: モバイルアプリケーション開発")
    print("Scenario: Mobile Application Development")
    print("=" * 80 + "\n")
    
    system = create_multi_expert_system()
    task = "クロスプラットフォーム対応のモバイルアプリ開発"
    
    results = system.delegate(task)
    print(results)


def run_all_scenarios():
    """全てのシナリオを実行"""
    scenarios = [
        ("1", "機械学習モデル", scenario_machine_learning),
        ("2", "セキュリティ対策", scenario_security),
        ("3", "マイクロサービス", scenario_microservices),
        ("4", "テスト自動化", scenario_testing),
        ("5", "データパイプライン", scenario_data_pipeline),
        ("6", "モバイルアプリ", scenario_mobile_app),
    ]
    
    print("\n" + "=" * 80)
    print("追加シナリオ集")
    print("Additional Scenarios Collection")
    print("=" * 80)
    print("\n利用可能なシナリオ:")
    for num, name, _ in scenarios:
        print(f"  {num}. {name}")
    print("  0. 全てのシナリオを実行")
    
    choice = input("\n選択 (0-6): ").strip()
    
    if choice == "0":
        for _, _, scenario_func in scenarios:
            scenario_func()
            input("\n次のシナリオに進むにはEnterキーを押してください...")
    else:
        for num, _, scenario_func in scenarios:
            if choice == num:
                scenario_func()
                break
        else:
            print("無効な選択です。")


if __name__ == "__main__":
    run_all_scenarios()
