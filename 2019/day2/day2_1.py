from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict

count = 0

inputs: List[int] = []
with open('input') as f:
    for line in f:
        inputs = list(map(int, line.strip().split(",")))

inputs[1] = 12
inputs[2] = 2
index = 0
while index < len(inputs):
    opcode = inputs[index]
    first = inputs[index+1]
    second = inputs[index+2]
    result = inputs[index+3]
    if opcode == 1:
        inputs[result] = inputs[first] + inputs[second]
    elif opcode == 2:
        inputs[result] = inputs[first] * inputs[second]
    elif opcode == 99:
        print(f"Index 0={inputs[0]}")
        exit(0)
    else:
        print("error in program")
        exit(1)
    index += 4

print(f"Did not find exit code 99: {inputs[0]}")
# too high: 5154075