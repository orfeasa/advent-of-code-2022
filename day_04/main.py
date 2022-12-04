import re


def are_pairs_containing(pair1: tuple[int, int], pair2: tuple[int, int]) -> bool:
    min1, max1 = pair1
    min2, max2 = pair2
    return (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2)


def are_pairs_overlapping(pair1: tuple[int, int], pair2: tuple[int, int]) -> bool:
    min1, max1 = pair1
    min2, max2 = pair2
    return (min1 <= min2 <= max1) or (min2 <= min1 <= max2)


def part_one(filename: str) -> int:
    assignments = parse_input(filename)
    count = 0
    for pair in assignments:
        if are_pairs_containing(pair[0], pair[1]):
            count += 1
    return count


def part_two(filename: str) -> int:
    assignments = parse_input(filename)
    count = 0
    for pair in assignments:
        if are_pairs_overlapping(pair[0], pair[1]):
            count += 1
    return count


def parse_input(filename: str) -> list[list[tuple[int, int]]]:
    assignments = []
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            a, b, c, d = map(int, re.findall(r"\d+", line))
            assignments.append([(a, b), (c, d)])
    return assignments


if __name__ == "__main__":
    input_path = "./day_04/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
