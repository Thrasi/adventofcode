from day1 import Day1 as Day
import unittest
from pathlib import Path


class TestDay1(unittest.TestCase):
    day = "1"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()

    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 11)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 1882714)

    def test_task2_1(self):
        self.assertEqual(Day.task2(self.test_task_input), 31)

    def test_task2(self):
        self.assertEqual(Day.task2(self.task_input), 19437052)
