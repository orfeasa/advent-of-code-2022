import ast
import operator
from functools import cmp_to_key, reduce


def part_one(filename: str) -> int:
    lines = parse_input(filename)
    return sum([i + 1 for i in range(len(lines)) if cmp_values(*lines[i]) == 1])


def part_two(filename: str) -> int:
    lines = parse_input(filename)
    keys = [[[2]], [[6]]]
    flat_lines = [item for sublist in lines for item in sublist]
    flat_lines.extend(keys)
    flat_lines.sort(key=cmp_to_key(cmp_values), reverse=True)
    return reduce(
        operator.mul, [ind + 1 for ind, x in enumerate(flat_lines) if x in keys]
    )


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf8") as f:
        return [
            [ast.literal_eval(line) for line in pair.strip().split("\n")]
            for pair in f.read().split("\n\n")
        ]


# returns 1 if values are in the right order, -1 if not, 0 if equal
def cmp_values(left: int | list, right: int | list) -> int:
    def cmp(left, right: int) -> int:
        return (left < right) - (left > right)

    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        return cmp(left, right)
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            if (cmp_val := cmp_values(left[i], right[i])) != 0:
                return cmp_val
        if len(left) == len(right):
            return 0
        return cmp(len(left), len(right))
    if isinstance(left, int) and isinstance(right, list):
        return cmp_values([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return cmp_values(left, [right])
    raise ValueError(f"Invalid types: {type(left)} and {type(right)}")


if __name__ == "__main__":
    input_path = "./day_13/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
