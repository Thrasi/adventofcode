from day3 import Day3 as Day
import unittest
from pathlib import Path


class TestDay3(unittest.TestCase):
    day = "3"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    task_input = "".join(
        Path(f"{day}/input.txt").read_text().splitlines()
    )  ## newlines are removed
    test_task2_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+don't()mul(32,64](mul(11,8)undo()?mul(8,5))"

    def test_extract_numbers(self):
        memory = "xxxmul(1,43)l,,,mul(1 , 2)mul(3,9)"
        self.assertEqual(Day.extract_numbers(memory), [(1, 43), (3, 9)])
        memory = ""
        self.assertEqual(Day.extract_numbers(memory), [])

    def test_extract_enabled_memory(self):
        memory = self.test_task2_input
        self.assertEqual(
            Day.extract_enabled_memory(memory), ["xmul(2,4)&mul[3,7]!^", "?mul(8,5))"]
        )
        memory = ""
        self.assertEqual(Day.extract_enabled_memory(memory), [])

    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 161)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 190604937)

    def test_task2_1(self):
        self.assertEqual(Day.task2(self.test_task2_input), 48)

    def test_task2(self):
        self.assertEqual(Day.task2(self.task_input), 82857512)
