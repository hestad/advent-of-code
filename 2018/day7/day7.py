from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Step:
    letter: str
    parents: List[str]

    def is_available(self):
        return len(self.parents) == 0

    def remove_parent(self, parent: str):
        if parent in self.parents:
            self.parents.remove(parent)


def find_available(steps: List[Step]) -> List[Step]:
    result: List[Step] = []
    for s in steps:
        if s.is_available():
            result.append(s)
    return result


def clear_parents(steps: List[Step], parent: str):
    for s in steps:
        s.remove_parent(parent)


def part1():
    steps: Dict[str, Step] = {}
    with open('day7.txt') as f:
        for line in f.readlines():
            s = line.split(' ')
            before = s[1].strip()
            after = s[7].strip()
            steps.setdefault(before, Step(before, []))
            steps.setdefault(after, Step(after, []))
            steps[after].parents.append(before)
    result = ""
    while len(steps) > 0:
        available = find_available(list(steps.values()))
        available.sort(key=lambda x: x.letter)
        letter = available[0].letter
        result += letter
        steps.pop(letter, None)
        del available[0]
        clear_parents(list(steps.values()), letter)
    return result


print(f"Day 7, part 1: {part1()}")
