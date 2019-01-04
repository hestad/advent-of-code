from typing import List


def read_input() -> List[int]:
    with open('day8.txt') as f:
        return list(map(int, f.readlines()[0].split(' ')))


def parse_input(input: List[int]) -> (int, int):
    children_count = input[0]
    metadata = input[1]
    total_sum = 0
    start_index = 2
    end_index = len(input) - metadata

    children = []
    for i in range(children_count):
        result = parse_input(input[start_index:end_index])
        start_index += result[1]
        children.append(result[0])

    if children_count == 0:
        metadata_sum: int = sum(input[start_index:start_index + metadata])
        total_sum += metadata_sum
    else:
        for x in input[start_index:start_index + metadata]:
            if x > children_count or x < 1:
                continue
            total_sum += children[x-1]

    return total_sum, start_index + metadata


def part2() -> int:
    return parse_input(read_input())[0]


print(f"2018, day 8, part2: {part2()}")  # 40292
