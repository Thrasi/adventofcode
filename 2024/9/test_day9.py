from day import Day
import unittest
from pathlib import Path


class TestDay9(unittest.TestCase):
    day = "9"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()

    def test_expand_disk_1(self):
        test_input = "12345"
        self.assertEqual(
            Day.expand_disk(test_input),
            [0, ".", ".", 1, 1, 1, ".", ".", ".", ".", 2, 2, 2, 2, 2],
        )

    def test_seek_index(self):
        disk = [0, ".", ".", 1]
        self.assertEqual(Day.seek_left(disk, len(disk) - 1), 3)
        disk = [0, ".", "."]
        self.assertEqual(Day.seek_left(disk, len(disk) - 1), 0)

    def test_defragment_disk(self):
        disk = [0, ".", ".", 1, 1, 1, ".", ".", ".", ".", 2, 2, 2, 2, 2]
        self.assertEqual(Day.defragment_disk(disk), [0, 2, 2, 1, 1, 1, 2, 2, 2])

    def test_checksum(self):
        test_disk = [int(char) for char in "0099811188827773336446555566"] + ["."]
        self.assertEqual(Day.checksum(test_disk), 1928)

    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 1928)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 6349606724455)

    # def test_defragment_disk_whole_files(self):
    #     disk = [
    #         char if char == "." else int(char)
    #         for char in "00...111...2...333.44.5555.6666.777.888899"
    #     ]
    #     print(disk)
    #     expected_disk = [
    #         char if char == "." else int(char)
    #         for char in "00992111777.44.333....5555.6666.....8888.."
    #     ]
    #     print(expected_disk)
    #     self.assertEqual(Day.defragment_disk_whole_files(disk), expected_disk)

    # def test_task2_1(self):
    #     self.assertEqual(Day.task2(self.test_task_input), 6)

    # def test_task2(self):
    #     self.assertEqual(Day.task2(self.task_input), 1888)
