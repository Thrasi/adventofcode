import re
from typing import List, Dict, Tuple

class Guard_map:
    def __init__(self, map_str: str):
        self.map = map_str.splitlines()
        self.obstructions = self.get_obstructions(self.map)

    def is_obstructed(self, position: Tuple[int, int]) -> bool:
        return self.map[position[0]][position[1]] == "#"

    def is_in_bounds(self, position: Tuple[int, int]) -> bool:
        return 0 <= position[0] < len(self.map) and 0 <= position[1] < len(self.map[0])

    def get_obstructions(self, map_rows: List[str]) -> List[Tuple[str, str]]:
        obstructions = set()
        for row_nr, row in enumerate(map_rows):
            for col_nr, col in enumerate(row):
                if col =="#":
                    obstructions.add((row_nr, col_nr))
        return obstructions


class Guard:
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }
    def __init__(self, map_str: str):
        self.map = Guard_map(map_str)
        self.row, self.col, self.direction = self.get_starting_position(self.map.map)
        self.visited = set()
        self.visited.add((self.row, self.col))

    def get_starting_position(self, map_rows: List[str]) -> Tuple[int, int, str]:
        for row_nr, row in enumerate(map_rows):
            for col_nr, col in enumerate(row):
                if col in ["^", "v", "<", ">"]:
                    return row_nr, col_nr, col
    
    def turnRight(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"

    def move(self):
        next_position = (self.row + Guard.directions[self.direction][0], self.col + Guard.directions[self.direction][1])
        while self.map.is_in_bounds(next_position) and not self.map.is_obstructed(next_position):
            self.row, self.col = next_position
            self.visited.add(next_position)
            next_position = (self.row + Guard.directions[self.direction][0], self.col + Guard.directions[self.direction][1])

        if self.map.is_in_bounds(next_position):
            self.turnRight()
        else:
            self.row, self.col = next_position
    
    def get_state(self) -> Tuple[int, int, str]:
        return (self.row, self.col, self.direction)

    def log(self):
        print(f"({self.row}, {self.col}), direction: {self.direction}")
        
    def is_in_bounds(self) -> bool:
        position = (self.row, self.col)
        return self.map.is_in_bounds(position)

class Day:

    def task1(task_input: str) -> int:
        guard = Guard(task_input)
        while guard.is_in_bounds():
            guard.move()
        
        return len(guard.visited)

    def is_cycle(guard: Guard) -> bool:
        states = set()
        state1 = guard.get_state()
        states.add(state1)
        while guard.is_in_bounds():
            guard.move()
            if guard.get_state() in states:
                return True
            else:
                states.add(guard.get_state())
        return False
            
    def task2(task_input: str) -> int:
        guard = Guard(task_input)
        pos1 = guard.col, guard.row
        state1 = guard.get_state()
        total = 0
        for row in range(len(guard.map.map)):
            print(f"{row/len(guard.map.map)}% done")
            for col in range(len(guard.map.map[0])):
                if (row, col) == pos1:
                    continue
                states = set()
                states.add(state1)
                guard = Guard(task_input)
                guard.map.map[row] = guard.map.map[row][:col]+"#"+guard.map.map[row][col+1:]
                if Day.is_cycle(guard):
                    total += 1
                
        return total