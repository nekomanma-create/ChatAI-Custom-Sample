#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit Tests for Multi-Expert System
"""

import unittest
from multi_expert_system import (
    Planner, Roger, Lewis, Sam, Daniel,
    create_multi_expert_system
)


class TestPlanner(unittest.TestCase):
    """Test cases for Planner class"""
    
    def setUp(self):
        self.planner = Planner()
    
    def test_planner_initialization(self):
        """Test planner initializes correctly"""
        self.assertEqual(self.planner.name, "Planner")
        self.assertEqual(len(self.planner.experts), 0)
    
    def test_register_expert(self):
        """Test expert registration"""
        roger = Roger()
        self.planner.register_expert(roger)
        self.assertIn("Roger", self.planner.experts)
        self.assertEqual(self.planner.experts["Roger"], roger)
    
    def test_plan_method(self):
        """Test plan method returns expected format"""
        task = "テストタスク"
        result = self.planner.plan(task)
        self.assertIn("Planner", result)
        self.assertIn(task, result)
    
    def test_delegate_with_no_experts(self):
        """Test delegation with no registered experts"""
        task = "タスク"
        result = self.planner.delegate(task)
        self.assertIn("Planner", result)
    
    def test_delegate_with_all_experts(self):
        """Test delegation with all experts registered"""
        self.planner.register_expert(Roger())
        self.planner.register_expert(Lewis())
        self.planner.register_expert(Sam())
        self.planner.register_expert(Daniel())
        
        task = "完全なタスク"
        result = self.planner.delegate(task)
        
        # Check all experts responded
        self.assertIn("Planner", result)
        self.assertIn("Roger", result)
        self.assertIn("Lewis", result)
        self.assertIn("Sam", result)
        self.assertIn("Daniel", result)


class TestRoger(unittest.TestCase):
    """Test cases for Roger class"""
    
    def setUp(self):
        self.roger = Roger()
    
    def test_roger_initialization(self):
        """Test Roger initializes correctly"""
        self.assertEqual(self.roger.name, "Roger")
        self.assertEqual(self.roger.role, "Engineering Leader")
    
    def test_respond_returns_code(self):
        """Test Roger's response contains code"""
        task = "APIエンドポイント実装"
        result = self.roger.respond(task)
        
        self.assertIn("Roger", result)
        self.assertIn("Engineering Leader", result)
        self.assertIn("```python", result)
        self.assertIn("def", result)
    
    def test_code_generation(self):
        """Test code generation includes task reference"""
        task = "データベース接続"
        code = self.roger._generate_code(task)
        
        self.assertIn(task, code)
        self.assertIn("def solve_task()", code)
        self.assertIn("def process_task()", code)


class TestLewis(unittest.TestCase):
    """Test cases for Lewis class"""
    
    def setUp(self):
        self.lewis = Lewis()
    
    def test_lewis_initialization(self):
        """Test Lewis initializes correctly"""
        self.assertEqual(self.lewis.name, "Lewis")
        self.assertEqual(self.lewis.role, "Sub-Leader / Code Explainer")
    
    def test_respond_returns_explanation(self):
        """Test Lewis's response contains explanation"""
        task = "コード最適化"
        result = self.lewis.respond(task)
        
        self.assertIn("Lewis", result)
        self.assertIn("解説", result)
    
    def test_explanation_content(self):
        """Test explanation contains key elements"""
        task = "テスト"
        explanation = self.lewis._explain_code(task)
        
        self.assertIn("関数構造", explanation)
        self.assertIn("設計の考え方", explanation)
        self.assertIn("実行フロー", explanation)


class TestSam(unittest.TestCase):
    """Test cases for Sam class"""
    
    def setUp(self):
        self.sam = Sam()
    
    def test_sam_initialization(self):
        """Test Sam initializes correctly"""
        self.assertEqual(self.sam.name, "Sam")
        self.assertEqual(self.sam.role, "Manager")
    
    def test_respond_returns_purpose_analysis(self):
        """Test Sam's response contains purpose analysis"""
        task = "プロジェクト計画"
        result = self.sam.respond(task)
        
        self.assertIn("Sam", result)
        self.assertIn("目的", result)
    
    def test_purpose_analysis_content(self):
        """Test purpose analysis contains key sections"""
        task = "新機能開発"
        analysis = self.sam._analyze_purpose(task)
        
        self.assertIn(task, analysis)
        self.assertIn("ビジネス価値", analysis)
        self.assertIn("技術的目標", analysis)
        self.assertIn("成功基準", analysis)


class TestDaniel(unittest.TestCase):
    """Test cases for Daniel class"""
    
    def setUp(self):
        self.daniel = Daniel()
    
    def test_daniel_initialization(self):
        """Test Daniel initializes correctly"""
        self.assertEqual(self.daniel.name, "Daniel")
        self.assertEqual(self.daniel.role, "Summarizer")
    
    def test_respond_returns_summary(self):
        """Test Daniel's response contains summary"""
        task = "レビュー"
        result = self.daniel.respond(task)
        
        self.assertIn("Daniel", result)
        self.assertIn("要点", result)
    
    def test_summary_content(self):
        """Test summary contains detailed points"""
        task = "総括"
        summary = self.daniel._create_summary(task)
        
        self.assertIn(task, summary)
        self.assertIn("要点まとめ", summary)
        self.assertIn("Roger", summary)
        self.assertIn("Lewis", summary)
        self.assertIn("Sam", summary)
        self.assertIn("まとめのまとめ", summary)


class TestMultiExpertSystem(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def test_create_multi_expert_system(self):
        """Test system creation includes all experts"""
        system = create_multi_expert_system()
        
        self.assertIsInstance(system, Planner)
        self.assertEqual(len(system.experts), 4)
        self.assertIn("Roger", system.experts)
        self.assertIn("Lewis", system.experts)
        self.assertIn("Sam", system.experts)
        self.assertIn("Daniel", system.experts)
    
    def test_full_workflow(self):
        """Test complete workflow from task to results"""
        system = create_multi_expert_system()
        task = "統合テスト用タスク"
        
        result = system.delegate(task)
        
        # Verify all components are present
        self.assertIn("Planner", result)
        self.assertIn("Roger", result)
        self.assertIn("Lewis", result)
        self.assertIn("Sam", result)
        self.assertIn("Daniel", result)
        
        # Verify task appears in result
        self.assertIn(task, result)
    
    def test_expert_order(self):
        """Test experts respond in correct order"""
        system = create_multi_expert_system()
        task = "順序テスト"
        
        result = system.delegate(task)
        
        # Find positions of each expert's response
        planner_pos = result.find("Planner")
        roger_pos = result.find("Roger")
        lewis_pos = result.find("Lewis")
        sam_pos = result.find("Sam")
        daniel_pos = result.find("Daniel")
        
        # Verify order: Planner -> Roger -> Lewis -> Sam -> Daniel
        self.assertTrue(planner_pos < roger_pos)
        self.assertTrue(roger_pos < lewis_pos)
        self.assertTrue(lewis_pos < sam_pos)
        self.assertTrue(sam_pos < daniel_pos)


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)
