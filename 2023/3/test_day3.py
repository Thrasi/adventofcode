import unittest
import sys, re
from day3 import Day3
 
class TestDay3(unittest.TestCase):
    def read_input(self, filename):
        with open(filename, "r") as f:
            return f.read()

    def test_span_has_symbol(self):
        cases = {
            ("617*......", (0, 3), True),
            ("617.+....", (0, 3), False),
            ("617.+...#", (7, 8), True)
        }
        for case in cases:
            line, span, expected = case
            self.assertEqual(Day3().span_has_symbol(span, line), expected)
    

    def test_overlap(self):
        spans = [ ((0, 3), (3, 4), False),
                  ((0, 3), (2, 4), True),
                  ((3, 5), (2, 3), False),
                  ((3, 5), (2, 4), True),
                  ((2, 5), (0, 3), True)
        ]

        for span1, span2, expected in spans:
            self.assertEqual(Day3().overlap(span1, span2), expected)


    def test_is_gear_1(self):
        lines_to_check = [
            "467..114..",
            "...*......",
            "..35..633."
        ]
        numbers_to_check = [list(re.finditer(Day3().number_pattern, line)) for line in lines_to_check]
        numbers_to_check = [number for number_line in numbers_to_check for number in number_line]
        star = list(re.finditer(r"\*", lines_to_check[1]))[0]
        star_span = Day3().get_increased_span(star.span())
        self.assertEqual(Day3().is_gear(star_span, numbers_to_check), True)

    def test_is_gear_2(self):
        lines_to_check = [
            "617*.2....", 
            ".....+.58."
        ]
        numbers_to_check = [list(re.finditer(Day3().number_pattern, line)) for line in lines_to_check]
        numbers_to_check = [number for number_line in numbers_to_check for number in number_line]
        star = list(re.finditer(r"\*", lines_to_check[0]))[0]
        star_span = Day3().get_increased_span(star.span())
        
        self.assertEqual(Day3().is_gear(star_span, numbers_to_check), False)

    def test_is_part_number(self):
        lines_to_check = [
            "617*......", 
            ".....+.58.", 
            "..592....."
            ]
        number = Day3().number_pattern.search(".....+.58.")
        self.assertEqual(Day3().is_part_number(number, lines_to_check), False)

        lines_to_check = [
            "617*...+..", 
            ".....+.58.", 
            "..592....."
            ]
        number = Day3().number_pattern.search(".....+.58.")
        self.assertEqual(Day3().is_part_number(number, lines_to_check), True)
        
    def test_task1_1(self):
        task_input = self.read_input("input/task_1_test_1.txt")
        self.assertEqual(Day3().task1(task_input), 4361)

    def test_task_1(self):
        task_input = self.read_input("input/input.txt")
        self.assertEqual(Day3().task1(task_input), 522726)

    def test_task2_1(self):
        task_input = self.read_input("input/task_1_test_1.txt")
        self.assertEqual(Day3().task2(task_input), 467835)


    def test_task_2(self):
        task_input = self.read_input("input/input.txt")
        self.assertEqual(Day3().task2(task_input), 81721933)