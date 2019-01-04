from typing import List


def read_input() -> List[int]:
    with open('day8.txt') as f:
        return list(map(int, f.readlines()[0].split(' ')))


def parse_input(input: List[int]) -> (int, int):
    children = input[0]
    metadata = input[1]
    total_sum = 0
    start_index = 2
    end_index = len(input) - metadata
    for i in range(children):
        result = parse_input(input[start_index:end_index])
        total_sum += result[0]
        start_index += result[1]

    metadataSum: int = sum(input[start_index:start_index + metadata])
    total_sum += metadataSum

    return total_sum, start_index + metadata


def part1() -> int:
    return parse_input(read_input())[0]


print(f"2018, day 8, part1: {part1()}")  # 48155
