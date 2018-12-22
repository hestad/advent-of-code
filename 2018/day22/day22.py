from typing import List

depth = 7863
targetX = 14
targetY = 760


def erosion_level(geologicIndex: int):
    return (geologicIndex + depth) % 20183


def geologic_index(indices: List[List[int]], x: int, y: int) -> int:
    if x == 0 and y == 0:
        return 0
    elif x == targetX and y == targetY:
        return 0
    elif y == 0:
        return 16807 * x
    elif x == 0:
        return 48271 * y
    else:
        return indices[y - 1][x] * indices[y][x - 1]


def populate_erotion_levels() -> List[List[int]]:
    result: List[List[int]] = [[0 for x in range(targetX + 1)] for y in range(targetY + 1)]
    for y in range(targetY + 1):
        for x in range(targetX + 1):
            result[y][x] = erosion_level(geologic_index(result, x, y))
    return result

def get_type_matrix():
    return [[y % 3 for y in x] for x in populate_erotion_levels()]

def part1():
    return sum(sum(get_type_matrix(), []))


print(part1()) # 11462
