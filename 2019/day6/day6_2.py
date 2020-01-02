from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class Planet:
    name: str
    parent: Optional[Planet]
    youCount: int
    santaCount: int


root = Planet("COM", [], 0, None)
planets: Dict[str, Planet] = {root.name: root}
with open('input') as f:
    for line in f:
        strippedLine = line.strip()
        parentName, childName = strippedLine.split(')')
        parent = planets.setdefault(parentName, Planet(parentName, None, 0, 0))
        child = planets.setdefault(childName, Planet(childName, parent, 0, 0))
        child.parent = parent

youPath: List[Planet] = [planets["YOU"].parent]
sanPath: List[Planet] = [planets["SAN"].parent]

you = youPath[0].parent
santa = sanPath[0].parent
while you != root or santa != root:
    if you != root:
        if you in sanPath:
            youCount = youPath[-1].youCount + 1
            print(f"Found you in santas path: you={youCount}, san={you.santaCount}")
            print(you.santaCount + youCount)
            exit(0)
        else:
            you.youCount = youPath[-1].youCount + 1
            youPath.append(you)
            you = you.parent
    if santa != root:
        if santa in youPath:
            sanCount = sanPath[-1].santaCount + 1
            print(f"Found santa in your path: you={you.youCount}, san={sanCount}")
            print(you.santaCount + you.youCount)
            exit(0)
        else:
            santa.santaCount = sanPath[-1].santaCount + 1
            sanPath.append(santa)
            santa = santa.parent
# 547 is correct
