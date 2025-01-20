from day import Day
import unittest
from pathlib import Path


class TestDay5(unittest.TestCase):
    day = "5"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()

    def test_get_valid_page_orders(self):
        test_instructions = [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47]
        ]
        expected = [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13]
        ]
        rules = Day.get_rules(self.test_task_input)
        self.assertEqual(Day.get_valid_page_orders(test_instructions, rules), expected)

    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 143)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 4135)

    def test_task2_1(self):
        self.assertEqual(Day.task2(self.test_task_input), 123)

    def test_task2(self):
        self.assertEqual(Day.task2(self.task_input), 5285)
