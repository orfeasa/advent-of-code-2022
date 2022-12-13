import ast
import operator
from functools import cmp_to_key, reduce


def part_one(filename: str) -> int:
    lines = parse_input(filename)
    return sum([ind for ind, line in enumerate(lines, 1) if cmp_values(*line) == 1])


def part_two(filename: str) -> int:
    lines = parse_input(filename)
    keys = [[[2]], [[6]]]
    flat_lines = keys + [item for sublist in lines for item in sublist]
    flat_lines.sort(key=cmp_to_key(cmp_values), reverse=True)
    return reduce(
        operator.mul, [ind for ind, x in enumerate(flat_lines, 1) if x in keys]
    )


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf8") as f:
        return [
            [ast.literal_eval(line) for line in pair.strip().split("\n")]
            for pair in f.read().split("\n\n")
        ]


# returns 1 if values are in the right order, -1 if not, 0 if equal
def cmp_values(left: int | list, right: int | list) -> int:
    match left, right:
        case int(), int():
            return (left < right) - (left > right)
        case list(), list():
            for cmp_val in map(cmp_values, left, right):
                if cmp_val:
                    return cmp_val
            return cmp_values(len(left), len(right))
        case int(), list():
            return cmp_values([left], right)
        case list(), int():
            return cmp_values(left, [right])
    raise ValueError(f"Invalid types: {type(left)} and {type(right)}")


if __name__ == "__main__":
    input_path = "./day_13/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
