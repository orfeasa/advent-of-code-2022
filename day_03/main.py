def get_priority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 38


def part_one(filename: str) -> int:
    with open(filename) as f:
        rugsacks = list(map(lambda line: line.strip(), f.readlines()))

    sum = 0
    for r in rugsacks:
        share_item = set(r[len(r) // 2 :]) & set(r[: len(r) // 2 :])
        sum += get_priority(share_item.pop())
    return sum


def part_two(filename: str) -> int:
    with open(filename) as f:
        rugsacks = list(map(lambda line: line.strip(), f.readlines()))
    sum = 0
    for i in range(0, len(rugsacks), 3):
        common = set(rugsacks[i]) & set(rugsacks[i + 1]) & set(rugsacks[i + 2])
        sum += get_priority(common.pop())
    return sum


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
