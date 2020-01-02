from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict

count=0
with open('input') as f:
    for line in f:
        number = int(line.strip())
        count += int(number/3)-2

print(count)

