from __future__ import annotations

from typing import List

original_inputs: List[int] = []

with open('input') as f:
    for line in f:
        original_inputs = list(map(int, line.strip().split(",")))

for noun in range(100):
    for verb in range(100):
        inputs = original_inputs.copy()
        inputs[1] = noun
        inputs[2] = verb
        index = 0
        while index < len(inputs) - 3:
            opcode = inputs[index]
            first = inputs[index + 1]
            second = inputs[index + 2]
            result = inputs[index + 3]
            if opcode == 1:
                inputs[result] = inputs[first] + inputs[second]
            elif opcode == 2:
                inputs[result] = inputs[first] * inputs[second]
            elif opcode == 99:
                if inputs[0] == 19690720:
                    print(f"Answer: {100 * noun + verb}")
                    exit(0)
            else:
                print("error in program")
                exit(1)
            index += 4
print(f"Error, program gave no results. inputs[0]={inputs[0]}")
