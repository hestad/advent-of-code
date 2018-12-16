from dataclasses import dataclass
from typing import List, Dict


class Step:
    letter: str
    parents: List[str]
    remainingTime: int  # Task 2 only
    started: bool  # Task 2 only

    def __init__(self, letter: str):
        self.letter = letter
        self.parents = []
        self.remainingTime = 60 + ord(letter.lower()) - 96
        self.started = False

    def is_available(self):
        return len(self.parents) == 0 and not self.started

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


def read_steps() -> List[Step]:
    steps: Dict[str, Step] = {}
    with open('day7.txt') as f:
        for line in f.readlines():
            s = line.split(' ')
            before = s[1].strip()
            after = s[7].strip()
            if before not in steps:
                steps.update({before: Step(before)})
            if after not in steps:
                steps.update({after: Step(after)})
            steps[after].parents.append(before)
    return list(steps.values())


def part1():
    steps = read_steps()
    result = ""
    while len(steps) > 0:
        available = find_available(list(steps))
        available.sort(key=lambda x: x.letter)
        letter = available[0].letter
        result += letter
        steps.remove(available[0])
        del available[0]
        clear_parents(list(steps), letter)
    return result


@dataclass
class Workers:
    steps: List[Step]

    def run_tick(self) -> List[Step]:
        result: List[Step] = []
        for step in reversed(self.steps):
            step.remainingTime -= 1
            if step.remainingTime < 1:
                result.append(step)
                self.steps.remove(step)
        return result

    def add_step(self, step: Step) -> bool:
        if len(self.steps) > 4:
            return False
        step.started = True
        self.steps.append(step)
        return True


def part2() -> int:
    steps: List[Step] = read_steps()
    workers = Workers([])
    result = ""
    tick = -1
    while len(steps) > 0:
        tick += 1
        for done in workers.run_tick():
            result += done.letter
            steps.remove(done)
            clear_parents(steps, done.letter)
        available = find_available(list(steps))
        available.sort(key=lambda x: x.letter)
        while len(available) > 0 and workers.add_step(available[0]):
            del available[0]

    return tick


print(f"Day 7, part 1: {part1()}")
print(f"Day 7, part 1: {part2()}")
