import re
from typing import List, Iterator


class Day4:
    xmas = re.compile(r"XMAS")
    samx = re.compile(r"SAMX")

    def rotate90(m: List[List[str]]) -> List[List[str]]:
        return list(map("".join, zip(*reversed(m))))

    def count_horizontal(m: List[List[str]]) -> int:
        one_dimentional_input = " ".join(m)
        xmas_count = len(Day4.xmas.findall(one_dimentional_input))
        samx_count = len(Day4.samx.findall(one_dimentional_input))
        return xmas_count + samx_count

    def count_vertical(m: List[List[str]]) -> int:
        m_transposed = list(map("".join, zip(*m)))
        return Day4.count_horizontal(m_transposed)

    def _count_diagonal(m: List[List[str]]) -> int:
        count = 0
        height = len(m)
        width = len(m[0])
        for i in range(height - 3):
            for j in range(0, width - 3):
                letters = m[i][j] + m[i + 1][j + 1] + m[i + 2][j + 2] + m[i + 3][j + 3]
                if letters == "XMAS" or letters == "SAMX":
                    count += 1
        return count

    def count_diagonal(task_input: List[List[str]]) -> int:
        m = task_input
        count = 0
        count += Day4._count_diagonal(m)
        rotated = Day4.rotate90(m)
        count += Day4._count_diagonal(rotated)
        return count

    def task1(task_input: str) -> int:
        m = task_input.splitlines()
        total = 0
        total += Day4.count_horizontal(m)
        total += Day4.count_vertical(m)
        total += Day4.count_diagonal(m)
        return total

    def extract_window(m: List[List[str]], i: int, j: int) -> Iterator[List[str]]:
        for row in m[i - 1 : i + 2]:
            yield row[j - 1 : j + 2]

    def check_xmas(window: List[str]) -> bool:
        return (
            window[0][0] == "M"
            and window[0][2] == "S"
            and window[1][1] == "A"
            and window[2][0] == "M"
            and window[2][2] == "S"
        )

    def check_all_xmas(window: List[str]) -> bool:
        for _ in range(0, 4):
            if Day4.check_xmas(window):
                return True
            window = Day4.rotate90(window)
        return False

    def task2(task_input: str) -> int:
        m = task_input.splitlines()
        height = len(m)
        width = len(m[0])
        count = 0
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                window = list(Day4.extract_window(m, i, j))
                if Day4.check_all_xmas(window):
                    count += 1

        return count
