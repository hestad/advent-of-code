from __future__ import annotations

import queue
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class Planet:
    name: str
    children: List[Planet]
    orbits: int
    parent: Optional[Planet]


root = Planet("COM", [], 0, None)
planets: Dict[str, Planet] = {root.name: root}
with open('input') as f:
    for line in f:
        strippedLine = line.strip()
        parentName, childName = strippedLine.split(')')
        parent = planets.setdefault(parentName, Planet(parentName, [], 1, None))
        child = planets.setdefault(childName, Planet(childName, [], 1, parent))
        parent.children.append(child)
        child.parent = parent

count = 0
queue: queue.Queue[Planet] = queue.Queue(0)
queue.put(root)
while not queue.empty():
    current = queue.get()
    current.orbits += 0 if current.parent is None else current.parent.orbits
    count += current.orbits
    for child in current.children:
        queue.put(child)

print(count)
# 301100 is the correct answer
