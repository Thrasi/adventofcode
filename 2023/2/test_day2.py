import unittest
import sys
from day2 import Day2

class TestDay2(unittest.TestCase):
    def read_input(self, filename):
        with open(filename, "r") as f:
            return f.read()
        
    def test_task1_1(self):
        task_input = self.read_input("input/task_1_test_1.txt")
        expected = 8
        self.assertEqual(Day2().task1(task_input), expected)
    
    def test_task1_alt(self):
        task_input = self.read_input("input/task_1_test_1.txt")
        expected = 8
        self.assertEqual(Day2().task1(task_input), expected)

    def test_task1(self):
        task_input = self.read_input("input/input.txt")
        print(f"\nRun results: {Day2().task1(task_input)}")

    def test_task2_1(self):
        task_input = self.read_input("input/task_1_test_1.txt")
        expected = 2286
        self.assertEqual(Day2().task2(task_input), expected)
    
    def test_task2(self):
        task_input = self.read_input("input/input.txt")
        print(f"\nRun results: {Day2().task2(task_input)}")