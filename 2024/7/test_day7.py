from day import Day
import unittest
from pathlib import Path


class TestDay7(unittest.TestCase):
    day = "7"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()

    def test_get_equation(self):
        test = "190: 10 19"
        expected = [190, 10, 19]
        self.assertEqual(Day.get_equation(test), expected)

    def test_can_be_constructed(self):

        true_tests = [
            [10, 5, 5],
            [3267, 81, 40, 27],
            [292, 11, 6, 16, 20],
            [190, 10, 19],
        ]
        false_tests = [
            [10, 5],
            [83, 17, 5],
            [156, 15, 6],
            [7290, 6, 8, 6, 15],
            [161011, 16, 10, 13],
            [192, 17, 8, 14],
            [21037, 9, 7, 18, 13],
        ]

        for test in true_tests:
            target = test[0]
            numbers = test[1:]
            self.assertTrue(Day.can_be_constructed(numbers, target, False))

        for test in false_tests:
            target = test[0]
            numbers = test[1:]
            self.assertFalse(Day.can_be_constructed(numbers, target, False))

    def test_concatenation(self):
        true_tests = [[156, 15, 6], [7290, 6, 8, 6, 15], [192, 17, 8, 14]]
        for test in true_tests:
            target = test[0]
            numbers = test[1:]
            print()
            print(f"Checking {numbers} for {target}")
            self.assertTrue(Day.can_be_constructed(numbers, target, True))

    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 3749)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 5512534574980)

    def test_task2_1(self):
        test_input = """156: 15 6
                        7290: 6 8 6 15
                        192: 17 8 14"""
        self.assertEqual(Day.task2(test_input), 11387 - 3749)

    def test_task2(self):
        self.assertEqual(Day.task2(self.task_input), 328790210468594)
