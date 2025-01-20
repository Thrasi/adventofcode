import re
from typing import List, Tuple


class Day3:
    mul_pattern = re.compile(r"mul\(([1-9][0-9]{,2}),([1-9][0-9]{,2})\)")
    start_enabled_pattern = re.compile(r".*?(?=don't\(\))")
    enabled_pattern = re.compile(r"(?<=do\(\)).*?(?=don't\(\)|$)")

    def extract_numbers(memory: str) -> List[Tuple[int, int]]:
        numbers = [tuple(map(int, pair)) for pair in Day3.mul_pattern.findall(memory)]
        return numbers

    def extract_enabled_memory(memory: str) -> List[str]:
        memory_start = Day3.start_enabled_pattern.search(memory)
        enabled_memory = []
        if memory_start:
            enabled_memory.append(memory_start.group(0))
            memory = memory[memory_start.end() :]

        enabled_memory.extend(Day3.enabled_pattern.findall(memory))
        return enabled_memory

    def task1(task_input: str) -> int:
        return sum(map(lambda x: x[0] * x[1], Day3.extract_numbers(task_input)))

    def task2(task_input: str) -> int:
        enabled_memory = Day3.extract_enabled_memory(task_input)
        total = 0
        for memory in enabled_memory:
            total += sum(map(lambda x: x[0] * x[1], Day3.extract_numbers(memory)))

        return total
