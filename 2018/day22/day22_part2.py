from dataclasses import dataclass
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


@dataclass
class Region:
    type: int
    neither: int
    torch: int
    climb: int

    def min_distance(self):
        return min(self.neither, self.torch, self.climb)


def create_regions():
    types = get_type_matrix()
    result: List[List[Region]] = [[None for x in range(len(types[0]))] for y in range(len(types))]
    result[0][0] = Region(0, 0, 0, 0)
    width = len(types[0])
    height = len(types)
    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                continue
            result[y][x] = Region(types[y][x], 1000000, 1000000, 1000000)
    return result


def neither_distance(from_region, to_region):
    if from_region.type == 0 or to_region.type == 0:
        return 1000000
    if from_region.type == to_region.type:
        return from_region.neither + 1
    return from_region.neither + 1 + 7


def torch_distance(from_region, toRegion):
    if from_region.type == 1 or toRegion.type == 1:
        return 1000000
    if from_region.type == toRegion.type:
        return from_region.neither + 1
    return from_region.neither + 1 + 7


def climb_distance(from_region, toRegion):
    if from_region.type == 2 or toRegion.type == 2:
        return 1000000
    if from_region.type == toRegion.type:
        return from_region.neither + 1
    return from_region.neither + 1 + 7


def update_neither(regions, x, y):
    region = regions[y][x]
    neither = 100000
    if x > 0:
        neither = neither_distance(regions[y][x - 1], region)
        print(f"neither_distance left {neither}, from={regions[y][x - 1]}, to={region}")
    if x < len(regions[0]) - 1:
        neither_right = neither_distance(regions[y][x + 1], region)
        print(f"neither_distance right {neither_right}, from={regions[y][x + 1]}, to={region}")
        if neither_right < neither:
            neither = neither_right
    if y > 0:
        neither_up = neither_distance(regions[y - 1][x], region)
        print(f"neither_distance up {neither_up}, from={regions[y][y - 1]}, to={region}")
        if neither_up < neither:
            neither = neither_up
    if y < len(regions) - 1:
        neither_down = neither_distance(regions[y + 1][x], region)
        print(f"neither_distance down {neither_down}, from={regions[y][y + 1]}, to={region}")
        if neither_down < neither:
            neither = neither_down
    regions[y][x].neither = neither


def update_torch(regions, x, y):
    region = regions[y][x]
    torch = 100000
    if x > 0:
        torch = torch_distance(regions[y][x - 1], region)
        print(f"torch_distance left {torch}, from={regions[y][x - 1]}, to={region}")
    if x < len(regions[0]) - 1:
        torch_right = torch_distance(regions[y][x + 1], region)
        print(f"torch_distance right {torch_right}, from={regions[y][x + 1]}, to={region}")
        if torch_right < torch:
            torch = torch_right
    if y > 0:
        torch_up = torch_distance(regions[y - 1][x], region)
        print(f"torch_distance up {torch_up}, from={regions[y][y - 1]}, to={region}")
        if torch_up < torch:
            torch = torch_up
    if y < len(regions) - 1:
        torch_down = torch_distance(regions[y + 1][x], region)
        print(f"torch_distance down {torch_down}, from={regions[y][y + 1]}, to={region}")
        if torch_down < torch:
            torch = torch_down
    regions[y][x].torch = torch


def update_climb(regions, x, y):
    region = regions[y][x]
    climb = 100000
    if x > 0:
        print(f"climb_distance left {climb}, from={regions[y][x - 1]}, to={region}")
        climb = climb_distance(regions[y][x - 1], region)
    if x < len(regions[0]) - 1:
        climb_right = climb_distance(regions[y][x + 1], region)
        print(f"climb_distance right {climb_right}, from={regions[y][x + 1]}, to={region}")
        if climb_right < climb:
            climb = climb_right
    if y > 0:
        climb_up = climb_distance(regions[y - 1][x], region)
        print(f"climb_distance up {climb_up}, from={regions[y][y - 1]}, to={region}")
        if climb_up < climb:
            climb = climb_up
    if y < len(regions) - 1:
        climb_down = climb_distance(regions[y + 1][x], region)
        print(f"climb_distance down {climb_down}, from={regions[y][y + 1]}, to={region}")
        if climb_down < climb:
            climb = climb_down
    regions[y][x].climb = climb


def printDistances(regions: List[List[Region]]):
    for line in regions:
        print([r.min_distance() for r in line])
    print("")
    print("")


def part2():
    regions = create_regions()
    width = len(regions[0])
    height = len(regions)
    for iteration in range(1):
        for y in range(height):
            for x in range(width):
                print(f"x={x},y={y}")
                if x == 0 and y == 0:
                    continue
                if x == 3:
                    exit(0)
                update_climb(regions, x, y)
                update_torch(regions, x, y)
                update_neither(regions, x, y)
        #printDistances(regions)
    return regions[targetY][targetX]


print(part2())
