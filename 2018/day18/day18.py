from typing import List


def read_input() -> List[List[str]]:
    result = []
    with open('day18.txt') as f:
        for line in f:
            result.append(list(line.strip()))
    return result


def count_adjacent(a: List[List[str]], resource_type: str, x: int, y: int) -> int:
    count = 0
    if len(a[0]) - 1 > x and a[y][x + 1] == resource_type:
        count += 1

    if x > 0 and a[y][x - 1] == resource_type:
        count += 1

    if len(a) - 1 > y and a[y + 1][x] == resource_type:
        count += 1

    if y > 0 and a[y - 1][x] == resource_type:
        count += 1

    if len(a) - 1 > y and len(a[0]) - 1 > x and a[y + 1][x + 1] == resource_type:
        count += 1

    if x > 0 and len(a) - 1 > y and a[y + 1][x - 1] == resource_type:
        count += 1

    if y > 0 and len(a[0]) - 1 > x and a[y - 1][x + 1] == resource_type:
        count += 1

    if y > 0 and x > 0 and a[y - 1][x - 1] == resource_type:
        count += 1
    return count


def find_next_state(area: List[List[str]], x: int, y: int) -> str:
    if area[y][x] == ".":
        trees = count_adjacent(area, "|", x, y)
        if trees > 2:
            return "|"
        return "."
    elif area[y][x] == "|":
        lumberyards = count_adjacent(area, "#", x, y)
        if lumberyards > 2:
            return "#"
        return "|"
    elif area[y][x] == "#":
        lumberyards = count_adjacent(area, "#", x, y)
        trees = count_adjacent(area, "|", x, y)
        if lumberyards < 1 or trees < 1:
            return "."
        return "#"
    else:
        print(f"invalid state: {area[y][x]}")
        exit(1)


def calculate_resource_value(area: List[List[str]]) -> int:
    lumberyards = sum(x.count('#') for x in area)
    trees = sum(x.count('|') for x in area)
    return trees * lumberyards


def iterate_one_minute(area, new_area):
    for y in range(len(area)):
        for x in range(len(area[0])):
            new_area[y][x] = find_next_state(area, x, y)


def part1() -> int:
    area = read_input()
    new_area = [[""] * len(area[0]) for _ in range(len(area))]
    for minute in range(1, 11):
        iterate_one_minute(area, new_area)
        area, new_area = new_area, area
    return calculate_resource_value(area)


def part2() -> int:
    area = read_input()
    new_area = [[""] * len(area[0]) for _ in range(len(area))]
    for minute in range(1, 1000):
        iterate_one_minute(area, new_area)
        area, new_area = new_area, area
        if minute > 550 and minute % 28 == 20:  # TODO Find recurring pattern by code
            return calculate_resource_value(area)


print(f"Day 18, Part 1: {part1()})")  # 637550
print(f"Day 18, Part 2: {part2()}")  # 201465
