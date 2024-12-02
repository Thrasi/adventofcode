import unittest
import sys
from day5 import Day5
 
class TestDay5(unittest.TestCase):
    def read_input(self, filename):
        with open(filename, "r") as f:
            return f.read()
        

    def test_map_1(self):
        mapping_rules = [
            [50, 98, 2],
            [52, 50, 48]
        ]
        self.assertEqual(Day5().map(0, mapping_rules), 0)
        self.assertEqual(Day5().map(98, mapping_rules), 50)
        self.assertEqual(Day5().map(99, mapping_rules), 51)
        self.assertEqual(Day5().map(53, mapping_rules), 55)
        self.assertEqual(Day5().map(200, mapping_rules), 200)

    def test_map_2(self):
        mapping_rules = [
            [0, 15, 37],
            [37, 52, 2],
            [39, 0, 15]
        ]
        self.assertEqual(Day5().map(81, mapping_rules), 81)
        self.assertEqual(Day5().map(14, mapping_rules), 53)
        self.assertEqual(Day5().map(57, mapping_rules), 57)
        self.assertEqual(Day5().map(13, mapping_rules), 52)

    def test_task1_1(self):
        task_input = self.read_input("input/test_input.txt")
        self.assertEqual(Day5().task1(task_input), 35)

    def test_task1(self):
        task_input = self.read_input("input/input.txt")
        self.assertEqual(Day5().task1(task_input), 388071289)


    def test_map_ranges(self):
        input_range = [0, 100]
        mapping_rules = [
            [52, 50, 48],
            [50, 98, 2]
            
        ]
        expected_output_ranges = [
            [0, 49],
            [52, 99],
            [50, 51],
            [100, 100]
        ]
        output_ranges = Day5().map_range(input_range, mapping_rules)
        print(f"output_ranges: {output_ranges}")
        self.assertEqual(output_ranges, expected_output_ranges)

    def test_task2_1(self):
        task_input = self.read_input("input/test_input.txt")
        self.assertEqual(Day5().task2(task_input), 46)

    # def test_task2(self):
    #     task_input = self.read_input("input/input.txt")
    #     self.assertEqual(Day5().task2(task_input), None)