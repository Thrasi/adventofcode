import unittest
import sys
from day4 import Day4
 
class TestDay4(unittest.TestCase):
    def read_input(self, filename):
        with open(filename, "r") as f:
            return f.read()
        
    def test_task1_1(self):
        task_input = self.read_input("input/test_input.txt")
        self.assertEqual(Day4().task1(task_input), 13)

    def test_task1(self):
        task_input = self.read_input("input/input.txt")
        self.assertEqual(Day4().task1(task_input), 19135)

    def test_task2_1(self):
        task_input = self.read_input("input/test_input.txt")
        self.assertEqual(Day4().task2(task_input), 30)

    def test_task2(self):
        task_input = self.read_input("input/input.txt")
        self.assertEqual(Day4().task2(task_input), 5704953)