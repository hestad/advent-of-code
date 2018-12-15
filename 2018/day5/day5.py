def is_opposite(a: str, b: str):
    return a != b and a.lower() == b.lower()


def read_file():
    with open('day5.txt') as f:
        return f.read().replace('\n', '')


def react(polymer: str):
    i = 0
    while i + 1 < len(polymer):
        if is_opposite(polymer[i], polymer[i + 1]):
            polymer = polymer[:i] + polymer[i + 2:]
            i = max(i - 1, 0)
        else:
            i += 1
    return polymer


def part1() -> int:
    return len(react(read_file()))


def part2() -> int:
    polymer = read_file()
    unique_letters = ''.join(set(polymer.lower()))
    min: int = len(polymer)
    for letter in unique_letters:
        truncated = polymer.replace(letter, '').replace(letter.upper(), '')
        size = len(react(truncated))
        if (size < min): min = size
    return min


print(f"Day 5, part 1: {part1()}")
print(f"Day 5, part 2: {part2()}")
