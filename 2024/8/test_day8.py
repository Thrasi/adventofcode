from day import Day, Antenna, Antenna_map, Antinode
import unittest
from pathlib import Path


class TestDay8(unittest.TestCase):
    day = "8"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()
    test_task_input_2 = Path(f"{day}/test_input_2.txt").read_text()
    test_task_input_3 = Path(f"{day}/test_input_3.txt").read_text()

    def test_get_antennas(self):
        expected = {
            "0": {
                Antenna(1, 8, "0"),
                Antenna(2, 5, "0"),
                Antenna(3, 7, "0"),
                Antenna(4, 4, "0"),
            },
            "A": {
                Antenna(5, 6, "A"),
                Antenna(8, 8, "A"),
                Antenna(9, 9, "A"),
            },
        }
        antenna_map = Antenna_map(self.test_task_input)
        self.assertEqual(antenna_map.antennas, expected)

    def test_get_antinodes(self):
        a = Antenna(3, 4, "a")
        b = Antenna(4, 8, "a")
        antenna_map = Antenna_map(self.test_task_input)
        antinodes = antenna_map.get_antinodes(a, b)
        expected = {Antinode(2, 0), Antinode(5, 12)}
        # print()
        # for antinode in antinodes:
        #     print(antinode)
        # print()
        # for e in expected:
        #     print(e)
        self.assertEqual(antinodes, expected)

    def test_calculate_antinodes(self):
        expected = {
            Antinode(1, 3),
            Antinode(2, 0),
            Antinode(6, 2),
            Antinode(7, 6),
        }
        test_input = Path(f"8/test_input_out.txt").read_text()
        antenna_map = Antenna_map(test_input)
        antinodes = antenna_map.calculate_antinodes("a")
        self.assertEqual(antinodes, expected)

        #     lines = test_input.splitlines()

        # print()
        # lines = self.test_task_input_2.splitlines()
        # for i, r in enumerate(lines):
        #     for j, c in enumerate(r):
        #         if c not in (
        #             ".",
        #             # "a",
        #             # "0",
        #             # "A",
        #         ):
        #             print(f"Antinode({i}, {j}),")

    def test_calculate_antinodes_part_2(self):
        expected = {
            Antinode(0, 0),
            Antinode(0, 5),
            Antinode(1, 3),
            Antinode(2, 1),
            Antinode(2, 6),
            Antinode(3, 9),
            Antinode(4, 2),
            Antinode(6, 3),
            Antinode(8, 4),
        }
        antenna_map = Antenna_map(self.test_task_input_2, harmonics=True)
        antinodes = antenna_map.calculate_antinodes("T")
        self.assertEqual(antinodes, expected)

    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 14)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 426)

    def test_task2_1(self):
        self.assertEqual(Day.task2(self.test_task_input_2), 9)

    def test_task2_2(self):
        self.assertEqual(Day.task2(self.test_task_input_3), 34)

    def test_task2(self):
        self.assertEqual(Day.task2(self.task_input), 1359)
