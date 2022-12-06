def part_one(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        stream = f.read().strip()
    return first_consecutive_unique(stream, 4)


def part_two(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        stream = f.read().strip()
    return first_consecutive_unique(stream, 14)


def first_consecutive_unique(stream: str, unique: int) -> int:
    for i in range(len(stream)):
        if len(stream[i : i + unique]) == len(set(stream[i : i + unique])):
            return i + unique
    return 0


if __name__ == "__main__":
    input_path = "./day_06/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
