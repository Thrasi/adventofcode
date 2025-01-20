import re
from typing import List, Dict, Tuple, Union, Generator, Any


class Block:
    def __init__(self, start: int, end: int, fileId: str):
        self.start = start
        self.end = end
        self.fileId = fileId
        self.size = end - start

    def is_empty(self) -> bool:
        return self.fileId == "."

    def checksum(self) -> int:
        if self.fileId == ".":
            return 0
        else:
            return sum(
                [index * int(self.fileId) for index in range(self.start, self.end)]
            )


class Day:

    @staticmethod
    def expand_disk(task_input: str) -> List[Union[str, int]]:
        print()
        disk_string = []
        for index, char in enumerate(task_input):
            segment_length = int(char)
            segmentId = index // 2
            segment = segment_length * [segmentId if index % 2 == 0 else "."]
            disk_string.extend(segment)
        return disk_string

    @staticmethod
    def seek_left(disk: List[Union[str, int]], index: int) -> int:
        return Day.seek(disk, index, -1)

    @staticmethod
    def seek_right(disk: List[Union[str, int]], index: int) -> int:
        return Day.seek(disk, index, 1)

    @staticmethod
    def seek(disk: List[Union[str, int]], index: int, direction: int) -> int:
        while disk[index] == ".":
            index = index + direction
        return index

    @staticmethod
    def defragment_disk(disk: List[Union[str, int]]) -> List[Union[str, int]]:
        index1 = 0
        index2 = Day.seek_left(disk, len(disk) - 1)
        while index1 < index2:
            if disk[index1] == ".":
                disk[index1] = disk[index2]
                disk[index2] = "."

            index1 += 1
            index2 = Day.seek_left(disk, index2)

        return disk[: index2 + 1]

    @staticmethod
    def checksum(disk: List[Union[str, int]]) -> int:
        return sum(
            [
                pos * int(fileIdNr)
                for pos, fileIdNr in enumerate(disk)
                if fileIdNr != "."
            ]
        )

    @staticmethod
    def task1(task_input: str) -> int:
        disk_string = Day.expand_disk(task_input)
        defragmented_disk = Day.defragment_disk(disk_string)
        return Day.checksum(defragmented_disk)

    @staticmethod
    def get_block(disk: List[Union[str, int]], index: int) -> Block:
        end = index
        fileId = disk[index]
        while index >= 0 and disk[index] == fileId:
            index -= 1
        start = index + 1
        return Block(start, end, str(fileId))

    @staticmethod
    def defragment_disk_whole_files(
        disk: List[Union[str, int]]
    ) -> List[Union[str, int]]:

        index = Day.seek_left(disk, len(disk) - 1)
        block_to_move = Day.get_block(disk, index)

        while block_to_move.start > 0:
            index = 0
            # get block large enoguh for last block between 0 and block_to_move.start

    @staticmethod
    def task2(task_input: str) -> int:
        return 0
