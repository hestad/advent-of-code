from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Set


def manhattan_distance(x: int, y: int):
    return abs(x) + abs(y)


cables: List[List[str]] = []
with open('input') as f:
    for line in f:
        cables.append(line.strip().split(","))

sets: List[Set[str]] = []
for cable in cables:
    result: Set[str] = set()
    x, y = 0, 0
    for dirs in cable:
        diff = int(dirs[1:])
        if dirs[0] == "R":
            for i in range(x, x + diff):
                result.add(f"{i},{y}")
            x += diff
        elif dirs[0] == "L":
            for i in range(x, x - diff,-1):
                result.add(f"{i},{y}")
            x -= diff
        elif dirs[0] == "U":
            for i in range(y, y + diff):
                result.add(f"{x},{i}")
            y += diff
        elif dirs[0] == "D":
            for i in range(y, y - diff,-1):
                result.add(f"{x},{i}")
            y -= diff
        else:
            print("wrong program")
            exit(1)
    sets.append(result)

intersection = sets[0].intersection(sets[1])
print(intersection)
for i in intersection:
    x = int(i.split(",")[0])
    y = int(i.split(",")[1])
    print(manhattan_distance(x, y))
# Answer; 2129