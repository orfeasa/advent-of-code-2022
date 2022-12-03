def get_priority(x: str) -> int:
    return ord(x) - ord("a") + 1 if x.islower() else ord(x) - ord("A") + 27


def part_one(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        sacks = f.read().strip().split("\n")

    priorities_sum = 0
    for r in sacks:
        mid: int = len(r) // 2
        common = set(r[mid:]) & set(r[:mid])
        priorities_sum += get_priority(common.pop())
    return priorities_sum


def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        sacks = f.read().strip().split("\n")

    priorities_sum = 0
    for i in range(0, len(sacks), 3):
        common = set(sacks[i]) & set(sacks[i + 1]) & set(sacks[i + 2])
        priorities_sum += get_priority(common.pop())
    return priorities_sum


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
