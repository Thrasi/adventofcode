import re
from typing import List, Dict, Tuple


class Day:

    @staticmethod
    def concatenate(a: int, b: int) -> int:
        return int(str(a) + str(b))

    @staticmethod
    def recursively_check(
        numbers: List[int], target: int, total: int, use_concat: bool
    ) -> bool:

        if len(numbers) == 1:
            return target in [total + numbers[0], total * numbers[0]] or (
                Day.concatenate(total, numbers[0]) == target if use_concat else False
            )

        # if (
        #     numbers[0] + total > target
        #     or numbers[0] * total > target
        #     or Day.concatenate(total, numbers[0]) > target
        # ):
        #     return False

        if Day.recursively_check(numbers[1:], target, total + numbers[0], use_concat):
            return True
        if Day.recursively_check(numbers[1:], target, total * numbers[0], use_concat):
            return True
        if use_concat and Day.recursively_check(
            numbers[1:], target, Day.concatenate(total, numbers[0]), use_concat
        ):
            return True

        return False

    @staticmethod
    def can_be_constructed(numbers: List[int], target: int, use_concat: bool) -> bool:
        return Day.recursively_check(numbers, target, 0, use_concat)

    @staticmethod
    def get_equation(equation_string: str) -> List[int]:
        strings = [equation_string.split(":")[0]] + equation_string.split(":")[
            1
        ].lstrip().split(" ")
        equation_numbers = list(map(int, strings))
        return equation_numbers

    @staticmethod
    def main(task_input: str, use_concat: bool) -> int:
        equations = [Day.get_equation(equation) for equation in task_input.splitlines()]
        total = 0
        for equation in equations:
            target = equation[0]
            numbers = equation[1:]
            if Day.can_be_constructed(numbers, target, use_concat):
                total += target

        return total

    @staticmethod
    def task1(task_input: str) -> int:
        return Day.main(task_input, False)

    @staticmethod
    def task2(task_input: str) -> int:
        return Day.main(task_input, True)
