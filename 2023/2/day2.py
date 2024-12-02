import re

class Day2:
    def __init__(self):
        self.red_pattern=re.compile(r"(\d+) red")
        self.green_pattern=re.compile(r"(\d+) green")
        self.blue_pattern=re.compile(r"(\d+) blue")
        self.pattern=re.compile(r"(\d+) (red|green|blue)")

    def task2(self, task_input):
        lines = task_input.split("\n")
        total_sum = 0
        for line_nr, line in enumerate(lines):
            red = max(list(map(int, re.findall(self.red_pattern, line))))
            green = max(list(map(int, re.findall(self.green_pattern, line))))
            blue = max(list(map(int, re.findall(self.blue_pattern, line))))
            total_sum += red * green * blue
        return total_sum


    def task1(self, task_input):
        lines = task_input.split("\n")
        red_cubes = 12
        green_cubes = 13
        blue_cubes = 14
        total_sum = 0
        for line_nr, line in enumerate(lines):
            if max(list(map(int, re.findall(self.red_pattern, line)))) > red_cubes:
                continue
            if max(list(map(int, re.findall(self.green_pattern, line)))) > green_cubes:
                continue
            if max(list(map(int, re.findall(self.blue_pattern, line)))) > blue_cubes:
                continue
            total_sum += line_nr+1
        return total_sum
    
    def task1_alt(self, task_input):
        lines = task_input.split("\n")
        red_cubes = 12
        green_cubes = 13
        blue_cubes = 14
        total_sum = 0


        for line_nr, line in enumerate(lines):
            draws = line.split(":")[1].split(";")
            blues = []
            reds = []
            greens = []
            for draw in draws:
                color_cubes = draw.split(",")
                for cube in color_cubes:
                    (number, color) = cube.strip().split(" ")
                    if color == "red":
                        reds.append(int(number))
                    elif color == "green":
                        greens.append(int(number))
                    elif color == "blue":
                        blues.append(int(number))
            if max(reds) > red_cubes:
                continue
            if max(greens) > green_cubes:
                continue
            if max(blues) > blue_cubes:
                continue

            total_sum += line_nr+1
        return total_sum
