from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict


def fuel(value):
    if value < 9:
        return 0
    req = int(value / 3) - 2
    return req + fuel(req)


assert fuel(100756) == 50346, str(fuel(100756))

count = 0
with open('input') as f:
    for line in f:
        number = int(line.strip())
        count += fuel(number)


print(count)
# too low: 5153952