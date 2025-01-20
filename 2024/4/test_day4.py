from day4 import Day4 as Day
import unittest
from pathlib import Path


class TestDay4(unittest.TestCase):
    day = "4"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    part2_test_input = Path(f"{day}/part2_test_input.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()
    test_task_input_1 = """..X...
.SAMX.
.A..A.
XMAS.S
.X....
"""

    test_task_input_2 = """...S...S
X.A.X.A.
.M...M..
X.A.X.A.
...S...S
"""

    def test_count_horizontal(self):
        test_data = ["XMASAMX.MM"]
        self.assertEqual(Day.count_horizontal(test_data), 2)
        self.assertEqual(Day.count_horizontal(self.test_task_input.splitlines()), 5)

    def test_count_vertical(self):
        self.assertEqual(Day.count_vertical(self.test_task_input.splitlines()), 3)
        test_vertical = Path("4/test_vertical.txt").read_text().splitlines()
        self.assertEqual(Day.count_vertical(test_vertical), 5)

    def test_count_diagonal(self):
        test_diagonal = Path("4/test_diagonal_1.txt").read_text().splitlines()
        self.assertEqual(Day.count_diagonal(test_diagonal), 8)

        test_diagonal = Path("4/test_diagonal_2.txt").read_text().splitlines()
        self.assertEqual(Day.count_diagonal(test_diagonal), 4)
        self.assertEqual(Day.count_diagonal(self.test_task_input_1.splitlines()), 1)
        self.assertEqual(Day.count_diagonal(self.test_task_input_2.splitlines()), 4)

    def testask1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 18)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 2530)

    def test_extract_window(self):
        m = self.part2_test_input.splitlines()
        self.assertEqual(
            list(Day.extract_window(m, 1, 1)),
            [".M.", "..A", ".M."],
        )

    def test_check_xmas(self):
        test_data = ["M.S", ".A.", "M.S"]
        self.assertTrue(Day.check_xmas(test_data))
        test_data = [".M.", "..A", ".M."]
        self.assertFalse(Day.check_xmas(test_data))

    def test_check_all_xmas(self):
        test_data = ["M.M", ".A.", "S.S"]
        self.assertTrue(Day.check_all_xmas(test_data))
        test_data = [".M.", "..A", ".M."]
        self.assertFalse(Day.check_all_xmas(test_data))

    def test_task2_1(self):
        self.assertEqual(Day.task2(self.part2_test_input), 9)

    def test_task2(self):
        self.assertEqual(Day.task2(self.task_input), 1921)
