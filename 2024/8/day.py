import re
from typing import List, Dict, Tuple, Set, Union


class Antinode:
    def __init__(self, row: int, column: int) -> None:
        self.r, self.c = row, column

    def __eq__(self, antenna) -> bool:
        return self.c == antenna.c and self.r == antenna.r

    def __hash__(self) -> int:
        return self.r * 1000 + self.c

    def __str__(self) -> str:
        return f"({self.r}, {self.c})"


class Antenna:
    def __init__(self, row: int, column: int, frequency: str) -> None:
        self.r, self.c, self.f = row, column, frequency

    def __eq__(self, antenna) -> bool:
        return self.c == antenna.c and self.r == antenna.r and self.f == antenna.f

    def __hash__(self) -> int:
        return self.r * 1000 + self.c


class Antenna_map:
    def __init__(self, input_string: str, harmonics: bool = False) -> None:
        self.input_string = input_string
        self.harmonics = harmonics
        lines = input_string.splitlines()
        self.height, self.width = len(lines), len(lines[0])
        self.frequencies = self._get_frequencies()
        self.antennas = self.get_antenna_dict()
        self.anti_nodes = self.calculate_all_antinodes()

    def _get_frequencies(self):
        freqs = set(self.input_string)
        freqs.discard("\n")
        freqs.discard(".")
        freqs.discard("#")
        return freqs

    def get_antenna_dict(self):
        all_antennas = dict()
        for frequency in self.frequencies:
            antennas = re.finditer(frequency, self.input_string.replace("\n", ""))
            antennas = {
                Antenna(
                    antenna.span()[0] // self.width,
                    antenna.span()[0] % self.width,
                    frequency,
                )
                for antenna in antennas
            }
            all_antennas[frequency] = antennas

        return all_antennas

    def in_bounds(self, position: Union[Antenna, Antinode]) -> bool:
        return 0 <= position.r < self.height and 0 <= position.c < self.width

    def get_antinodes(self, antenna1: Antenna, antenna2: Antenna) -> Set[Antinode]:
        antinodes = set()
        dc, dr = antenna2.c - antenna1.c, antenna2.r - antenna1.r

        if self.harmonics:
            antinode = Antinode(antenna1.r, antenna1.c)
            while self.in_bounds(antinode):
                antinodes.add(antinode)
                antinode = Antinode(antinode.r - dr, antinode.c - dc)

            antinode = Antinode(antenna2.r, antenna2.c)
            while self.in_bounds(antinode):
                antinodes.add(antinode)
                antinode = Antinode(antinode.r + dr, antinode.c + dc)
        else:
            antinodes.add(Antinode(antenna1.r - dr, antenna1.c - dc))
            antinodes.add(Antinode(antenna2.r + dr, antenna2.c + dc))

        return antinodes

    def calculate_antinodes(
        self, frequency: str, harmonics: bool = False
    ) -> Set[Antenna]:
        antennas = self.antennas[frequency]
        anti_nodes = set()
        for i, antenna in enumerate(list(antennas)):
            for antenna2 in list(antennas)[i + 1 :]:
                antinodes = {
                    antinode
                    for antinode in self.get_antinodes(antenna2, antenna)
                    if self.in_bounds(antinode)
                }
                anti_nodes.update(antinodes)
        return anti_nodes

    def calculate_all_antinodes(self, harmonics: bool = False) -> Set[Antenna]:
        anti_nodes = set()
        for frequency in self.frequencies:
            anti_nodes.update(self.calculate_antinodes(frequency, harmonics))
        return anti_nodes


class Day:
    @staticmethod
    def task1(task_input: str) -> int:
        antenna_map = Antenna_map(task_input)
        return len(antenna_map.anti_nodes)

    @staticmethod
    def task2(task_input: str) -> int:
        antenna_map = Antenna_map(task_input, harmonics=True)
        return len(antenna_map.anti_nodes)


if __name__ == "__main__":

    pass
