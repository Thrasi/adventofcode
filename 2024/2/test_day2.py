from day2 import Day2 as Day
import unittest
from pathlib import Path


class TestDay2(unittest.TestCase):
    day = "2"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()

    def test_report_is_safe(self):

        report = list(map(int, "7 6 4 2 1".split()))
        self.assertTrue(Day.report_is_safe(report))
        report = list(map(int, "1 2 7 8 9".split()))
        self.assertFalse(Day.report_is_safe(report))
        report = list(map(int, "1 3 2 4 5".split()))
        self.assertFalse(Day.report_is_safe(report))
        report = list(map(int, "8 6 4 1 1".split()))
        self.assertFalse(Day.report_is_safe(report))

    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 2)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 516)

    def test_task2_1(self):
        self.assertEqual(Day.task2(self.test_task_input), 4)

    def test_task2(self):
        self.assertEqual(Day.task2(self.task_input), 561)
