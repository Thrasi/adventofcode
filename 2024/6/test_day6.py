from day import Day, Guard
import unittest
from pathlib import Path


class TestDay6(unittest.TestCase):
    day = "6"
    test_task_input = Path(f"{day}/test_input.txt").read_text()
    test_task_input_2 = Path(f"{day}/test_input_2.txt").read_text()
    test_task_input_3 = Path(f"{day}/test_input_3.txt").read_text()
    task_input = Path(f"{day}/input.txt").read_text()


    def test_guard(self):
        guard = Guard(self.test_task_input)
        self.assertEqual(guard.col, 4)
        self.assertEqual(guard.row, 6)
        self.assertEqual(guard.direction, "^")

    def test_get_obstructions(self):
        guard = Guard(self.test_task_input)
        self.assertEqual(guard.map.obstructions, {(0, 4),(1,9),(3,2),(4,7),(6,1),(7,8),(8,0),(9,6)})

    def test_move(self):
        guard = Guard(self.test_task_input)
        guard.move()
        self.assertEqual(guard.row, 1)
        self.assertEqual(guard.col, 4)
        self.assertEqual(guard.visited, {(6,4),(5,4),(4,4),(3,4),(2,4),(1,4)})
        self.assertEqual(guard.direction, ">")

        guard.move()
        self.assertEqual(guard.row, 1)
        self.assertEqual(guard.col, 8)
        self.assertEqual(guard.visited, {(6,4),(5,4),(4,4),(3,4),(2,4),(1,4),(1,5),(1,6),(1,7),(1,8)})
        self.assertEqual(guard.direction, "v")

    def test_move_out_of_bounds(self):
        guard = Guard(self.test_task_input_2)
        guard.move()
        self.assertEqual(guard.row, 10)
        self.assertEqual(guard.col, 7)
        self.assertEqual(guard.direction, "v")


    def test_task1_1(self):
        self.assertEqual(Day.task1(self.test_task_input), 41)

    def test_task1(self):
        self.assertEqual(Day.task1(self.task_input), 5129)

    def test_is_cycle(self):
        guard = Guard(self.test_task_input_3)
        self.assertTrue(Day.is_cycle(guard))

    def test_task2_1(self):
        self.assertEqual(Day.task2(self.test_task_input), 6)

    def test_task2(self):
        self.assertEqual(Day.task2(self.task_input), 1888)
