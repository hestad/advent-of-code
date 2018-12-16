from collections import defaultdict
from dataclasses import dataclass
from types import FunctionType
from typing import List, Dict, Set


def addr(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a] + r[b]
    return r


def addi(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a] + b
    return r


def mulr(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a] * r[b]
    return r


def muli(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a] * b
    return r


def banr(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a] & r[b]
    return r


def bani(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a] & b
    return r


def borr(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a] | r[b]
    return r


def bori(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a] | b
    return r


def setr(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = r[a]
    return r


def seti(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = a
    return r


def gtir(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = 1 if a > r[b] else 0
    return r


def gtri(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = 1 if r[a] > b else 0
    return r


def gtrr(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = 1 if r[a] > r[b] else 0
    return r


def eqir(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = 1 if a == r[b] else 0
    return r


def eqri(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = 1 if r[a] == b else 0
    return r


def eqrr(register: List[int], a: int, b: int, c: int):
    r = register.copy()
    r[c] = 1 if r[a] == r[b] else 0
    return r


opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


@dataclass
class Sample:
    before: List[int]
    instructions: List[int]
    after: List[int]


def read_samples() -> List[Sample]:
    samples = []
    with open('day16_part1.txt') as f:
        lines = f.readlines()
        for sample in [lines[i:i + 4] for i in range(0, len(lines), 4)]:
            before: List[int] = eval(sample[0].split(': ')[1])
            instructions: List[int] = list(map(int, sample[1].split(' ')))
            after: List[int] = eval(sample[2].split(':  ')[1])
            samples.append(Sample(before, instructions, after))
    return samples


def part1():
    three_or_more = 0
    samples = read_samples()
    for sample in samples:
        opcode_count = 0
        for opcode in opcodes:
            if opcode(sample.before, sample.instructions[1], sample.instructions[2],
                      sample.instructions[3]) == sample.after:
                opcode_count += 1
        if opcode_count > 2:
            three_or_more += 1
    return three_or_more


def potential_opcodes() -> Dict[int, Set[FunctionType]]:
    samples = read_samples()
    known_opcodes: Dict[int, Set[FunctionType]] = defaultdict(set)
    for sample in samples:
        for opcode in opcodes:
            if opcode(sample.before, sample.instructions[1], sample.instructions[2],
                      sample.instructions[3]) == sample.after:
                known_opcodes[sample.instructions[0]].add(opcode)
    return known_opcodes


def remove_opcode(opcode_to_functions: Dict[int, Set[FunctionType]], opcode: FunctionType) \
        -> Dict[int, Set[FunctionType]]:
    for key, value in opcode_to_functions.items():
        value.discard(opcode)
    return opcode_to_functions


def work_out_opcodes() -> Dict[int, FunctionType]:
    # TODO rewrite when sober.
    result = {}
    opcode_to_functions: Dict[int, Set[FunctionType]] = potential_opcodes()
    while len(opcode_to_functions) > 0:
        for key, value in opcode_to_functions.items():
            if len(value) == 1:
                opcode = value.pop()
                result.update({key: opcode})
                for k, v in opcode_to_functions.items():
                    v.discard(opcode)
                del opcode_to_functions[key]
                break
    return result


@dataclass()
class Instruction:
    opcode: FunctionType
    a: int
    b: int
    c: int


def read_instructions() -> List[Instruction]:
    number_to_opcode: Dict[int, FunctionType] = work_out_opcodes()
    instructions = []
    with open('day16_part2.txt') as f:
        for line in f:
            s = list(map(int, line.strip().split(' ')))
            instructions.append(Instruction(number_to_opcode[s[0]], s[1], s[2], s[3]))
    return instructions


def part2():
    instructions: List[Instruction] = read_instructions()
    register = [0, 0, 0, 0]
    for i in instructions:
        register = i.opcode(register, i.a, i.b, i.c)
    return register


print(f"Day 16, part 1: {part1()}")  # 544
print(f"Day 16, part 1: {part2()}")  # [600, 600, 2, 2]
