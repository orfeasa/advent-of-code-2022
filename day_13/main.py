import ast
import operator
from functools import cmp_to_key, reduce


def part_one(filename: str) -> int:
    with open(filename, "r", encoding="utf8") as f:
        lines = [
            [ast.literal_eval(line) for line in pair.strip().split("\n")]
            for pair in f.read().split("\n\n")
        ]
    return sum([i + 1 for i in range(len(lines)) if are_values_ordered(*lines[i])])


def part_two(filename: str) -> int:
    with open(filename, "r", encoding="utf8") as f:
        lines = [
            [ast.literal_eval(line) for line in pair.strip().split("\n")]
            for pair in f.read().split("\n\n")
        ]
    flat_lines = [item for sublist in lines for item in sublist]
    keys = [[[2]], [[6]]]
    flat_lines.extend(keys)
    flat_lines.sort(key=cmp_to_key(are_values_ordered_cmp), reverse=True)
    return reduce(
        operator.mul, [ind + 1 for ind, x in enumerate(flat_lines) if x in keys]
    )


def are_values_ordered_cmp(left: int | list, right: int | list) -> int:
    match are_values_ordered(left, right):
        case True:
            return 1
        case False:
            return -1
        case None:
            return 0


def are_values_ordered(left: int | list, right: int | list) -> bool | None:
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            if (cmp := are_values_ordered(left[i], right[i])) is not None:
                return cmp
        if len(left) == len(right):
            return None
        return len(left) < len(right)
    if isinstance(left, int) and isinstance(right, list):
        return are_values_ordered([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return are_values_ordered(left, [right])
    raise ValueError(f"Invalid types: {type(left)} and {type(right)}")


if __name__ == "__main__":
    input_path = "./day_13/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
