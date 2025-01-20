from day import Day
import unittest
from pathlib import Path


class TestDay9(unittest.TestCase):
    day = "10"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()

    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 3749)

    # def test_task1(self):
    #     self.assertEqual(Day.task1(self.task_input), 5129)

    # def test_task2_1(self):
    #     self.assertEqual(Day.task2(self.test_task_input), 6)

    # def test_task2(self):
    #     self.assertEqual(Day.task2(self.task_input), 1888)
