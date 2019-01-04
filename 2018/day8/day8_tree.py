from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    children: List[any]
    metadata: List[int]

    def metadata_sum(self) -> int:
        return sum(self.metadata)

    def has_no_children(self) -> bool:
        return len(self.children) == 0

    def children_count(self):
        return len(self.children)


def read_input() -> List[int]:
    with open('day8.txt') as f:
        return list(map(int, f.readlines()[0].split(' ')))


def read_tree(input: List[int]) -> (Node, int):
    metadata = input[1]
    start_index = 2
    end_index = len(input) - metadata
    children = []
    for i in range(input[0]):
        result = read_tree(input[start_index:end_index])
        children.append(result[0])
        start_index += result[1]

    return Node(children, input[start_index:start_index + metadata]), start_index + metadata


def tree_metadata_sum(node: Node) -> int:
    total_sum = 0
    for child in node.children:
        total_sum += tree_metadata_sum(child)
    return total_sum + node.metadata_sum()


def part1() -> int:
    root = read_tree(read_input())[0]
    return tree_metadata_sum(root)


def tree_value(node: Node) -> int:
    total_sum = 0
    childrenValues = []
    for child in node.children:
        childrenValues.append(tree_value(child))

    if node.has_no_children():
        total_sum += node.metadata_sum()
    else:
        for x in node.metadata:
            if x > node.children_count() or x < 1:
                continue
            total_sum += childrenValues[x - 1]

    return total_sum


def part2() -> int:
    root = read_tree(read_input())[0]
    return tree_value(root)


print(f"2018, day 8, part1: {part1()}")  # 48155
print(f"2018, day 8, part2: {part2()}")  # 40292
