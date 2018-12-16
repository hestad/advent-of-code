from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Coordinate:
    point: Point
    distances: List[List[int]]


def manhattan_distance(a: Point, b: Point) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def read_points() -> List[Point]:
    result: List[Point] = []
    with open('day6.txt') as f:
        for line in f.readlines():
            s = line.split(', ')
            result.append(Point(int(s[0]), int(s[1])))
    return result


def boundaries(points: List[Point]):
    x_max, y_max = 0, 0
    for p in points:
        if p.x > x_max: x_max = p.x
        if p.y > y_max: y_max = p.y
    return x_max, y_max


def distances(p: Point, w: int, h: int) -> List[List[int]]:
    return [[manhattan_distance(p, Point(x, y)) for x in range(w)] for y in range(h)]


def read_coordinates() -> List[Coordinate]:
    points = read_points()
    width, height = boundaries(points)
    return [Coordinate(p, distances(p, width, height)) for p in points]


def closest(coordinates: List[Coordinate], x, y):
    min_distance = 100000
    min_distance_index = None
    for idx, val in enumerate(coordinates):
        distance = val.distances[y][x]
        if distance < min_distance:
            min_distance = distance
            min_distance_index = idx
    return min_distance_index


def is_border(x, y, width, height):
    return x == 0 or y == 0 or x + 1 == width or y + 1 == height


def part1():
    coordinates = read_coordinates()
    results = [0 for x in range(len(coordinates))]
    height, width = len(coordinates[0].distances), len(coordinates[0].distances[0])
    for y in range(height):
        for x in range(width):
            idx = closest(coordinates, x, y)
            if is_border(x, y, width, height):
                results[idx] = -1
            elif results[idx] == -1:
                continue
            else:
                results[idx] += 1

    return max(results)


def is_within(coordinates: List[Coordinate], x, y) -> bool:
    total_distance = 0
    for c in coordinates:
        total_distance += c.distances[y][x]
    if total_distance < 10000:
        return True
    return False


def part2():
    coordinates = read_coordinates()
    results = [0 for x in range(len(coordinates))]
    height, width = len(coordinates[0].distances), len(coordinates[0].distances[0])
    regions = 0
    for y in range(height):
        for x in range(width):
            if is_within(coordinates, x, y): regions += 1

    return regions


print(f"Day 6, part 1: {part1()}")
print(f"Day 6, part 1: {part2()}")
