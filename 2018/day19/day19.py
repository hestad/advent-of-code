from dataclasses import dataclass
from types import FunctionType
from typing import List


def addr(r: List[int], a: int, b: int, c: int):
    r[c] = r[a] + r[b]


def addi(r: List[int], a: int, b: int, c: int):
    r[c] = r[a] + b


def mulr(r: List[int], a: int, b: int, c: int):
    r[c] = r[a] * r[b]


def muli(r: List[int], a: int, b: int, c: int):
    r[c] = r[a] * b


def banr(r: List[int], a: int, b: int, c: int):
    r[c] = r[a] & r[b]


def bani(r: List[int], a: int, b: int, c: int):
    r[c] = r[a] & b


def borr(r: List[int], a: int, b: int, c: int):
    r[c] = r[a] | r[b]


def bori(r: List[int], a: int, b: int, c: int):
    r[c] = r[a] | b


def setr(r: List[int], a: int, b: int, c: int):
    r[c] = r[a]


def seti(r: List[int], a: int, b: int, c: int):
    r[c] = a


def gtir(r: List[int], a: int, b: int, c: int):
    r[c] = 1 if a > r[b] else 0


def gtri(r: List[int], a: int, b: int, c: int):
    r[c] = 1 if r[a] > b else 0


def gtrr(r: List[int], a: int, b: int, c: int):
    r[c] = 1 if r[a] > r[b] else 0


def eqir(r: List[int], a: int, b: int, c: int):
    r[c] = 1 if a == r[b] else 0


def eqri(r: List[int], a: int, b: int, c: int):
    r[c] = 1 if r[a] == b else 0


def eqrr(r: List[int], a: int, b: int, c: int):
    r[c] = 1 if r[a] == r[b] else 0


@dataclass
class Instruction:
    function: FunctionType
    a: int
    b: int
    c: int


def read_input() -> List[Instruction]:
    result = []
    with open('day19.txt') as f:
        for line in f:
            if "#ip" in line or len(line.strip()) == 0:
                continue
            s = line.split(' ')
            result.append(Instruction(eval(s[0]), int(s[1]), int(s[2]), int(s[3])))
    return result


ip_reg = 4
ip = 0
instructions = read_input()
register = [0, 0, 0, 0, 0, 0]
while -1 < ip < len(instructions):
    i = instructions[ip]
    register[ip_reg] = ip
    i.function(register, i.a, i.b, i.c)
    ip = register[ip_reg]
    ip += 1

print(register)