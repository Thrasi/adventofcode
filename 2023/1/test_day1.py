import unittest
import sys
from day1 import Day1

class TestDay1(unittest.TestCase):
    def read_input(self, filename):
        with open(filename, "r") as f:
            return f.read()

    def test_extract_first_and_last_number(self):
        test_cases = [
            ("abc123def", 13),
            ("abc1def", 11),
            ("abcdef", None),
        ]
        for case in test_cases:
            self.assertEqual(Day1().extract_first_and_last_number(case[0]), case[1])

    def test_find_first_occurence_of_number(self):
        test_cases = [
            ("abc123def", "1"),
            ("abcone2def", "1"),
            ("abcdef", None),
        ]
        for case in test_cases:
            self.assertEqual(Day1().find_first_occurence_of_number(case[0]), case[1])

        test_cases = [
            ("abc123def", "3"),
            ("abcone2three", "3"),
            ("abcdef", None),
        ]
        for case in test_cases:
            self.assertEqual(Day1().find_first_occurence_of_number(case[0], reverse=True), case[1])

    def test_extract_first_and_last_number_with_words(self):
        test_cases = [
            ("two1nine", 29),
            ("eightwothree", 83),
            ("abcone2threexyz", 13),
            ("xtwone3four", 24),
            ("4nineeightseven2", 42),
            ("zoneight234", 14),
            ("7pqrstsixteen", 76)
        ]
        for case in test_cases:
            self.assertEqual(Day1().extract_first_and_last_number_with_words(case[0]), case[1])

    def test_task1_1(self):
        task_input = self.read_input("input/task_1_test_1.txt")
        expected = 142
        self.assertEqual(Day1().task1(task_input), expected)

    def test_task1_2(self):
        task_input = self.read_input("input/task_1_test_2.txt")
        expected = 154
        self.assertEqual(Day1().task1(task_input), expected)

    def test_task2_1(self):
        task_input = self.read_input("input/task_2_test_1.txt")
        expected = 281
        self.assertEqual(Day1().task2(task_input), expected)

    def test_task1_run(self):
        task_input = self.read_input("input/input.txt")
        print(f"\nRun results: {Day1().task1(task_input)}")

    def test_task2_run(self):
        task_input = self.read_input("input/input.txt")
        print(f"\nRun results: {Day1().task2(task_input)}")