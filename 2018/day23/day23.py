from dataclasses import dataclass
from typing import List


@dataclass
class Bot:
    x: int
    y: int
    z: int
    range: int


def read_input() -> List[Bot]:
    result = []
    with open('day23.txt') as f:
        for line in f:
            s = line.split('>, r=')
            left = s[0].strip("pos=<")
            c = left.split(',')
            result.append(Bot(int(c[0]), int(c[1]), int(c[2]), int(s[1])))
    return result


def find_strongest(bots: List[Bot]) -> Bot:
    return max(bots, key=(lambda x: x.range))


def find_distance(a: Bot, b: Bot):
    x_dist = abs(a.x - b.x)
    y_dist = abs(a.y - b.y)
    z_dist = abs(a.z - b.z)
    return x_dist + y_dist + z_dist


def part1():
    bots = read_input()
    strongest = find_strongest(bots)
    print(strongest)
    return sum(map((lambda x: 0 if find_distance(strongest, x) > strongest.range else 1), bots))


print(f"Day 23, part1: {part1()}")  # 326
