class Day1:
    def get_columns(lines):
        column1 = []
        column2 = []
        for line in lines:
            split_line = [int(n) for n in line.split()]
            column1.append(split_line[0])
            column2.append(split_line[1])
        return column1, column2

    def task1(task_input: str) -> int:
        lines = task_input.splitlines()
        column1, column2 = Day1.get_columns(lines)

        sorted_column1 = sorted(column1)
        sorted_column2 = sorted(column2)
        sum = 0
        for a, b in zip(sorted_column1, sorted_column2):
            sum += abs(b - a)
        return sum

    def task2(task_input: str) -> int:
        lines = task_input.splitlines()
        column1, column2 = Day1.get_columns(lines)
        int_map = {}
        for number in column2:
            int_map[number] = int_map.get(number, 0) + 1
        sum = 0
        for number in column1:
            if number in int_map:
                sum += int_map[number] * number

        return sum
