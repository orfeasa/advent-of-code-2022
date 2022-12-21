import operator
from typing import Any

import sympy as sym


def part_one(filename: str) -> int:
    monkeys = parse_input(filename)
    return int(calc_monkey_val("root", monkeys))


def part_two(filename: str) -> int:
    monkeys = parse_input(filename)
    monkeys["humn"] = sym.Symbol("x")
    m1, _, m2 = (
        monkeys["root"].split(" ") if isinstance(monkeys["root"], str) else ("", "", "")
    )
    return int(
        sym.solve(
            calc_monkey_val(m2, monkeys) - calc_monkey_val(m1, monkeys), monkeys["humn"]
        )[0]
    )


def parse_input(filename: str) -> dict[str, Any]:
    with open(filename, encoding="utf-8") as f:
        monkeys: dict[str, int | str] = {
            line.strip().split(": ")[0]: line.strip().split(": ")[1]
            for line in f.readlines()
        }

    for monkey, val in monkeys.items():
        if isinstance(val, str) and len(val.split(" ")) == 1:
            monkeys[monkey] = int(val)
    return monkeys


def calc_monkey_val(monkey: str, monkeys: dict) -> int | float | sym.Symbol:
    if isinstance(monkeys[monkey], (int, sym.Symbol)):
        return monkeys[monkey]

    m1, _, m2 = monkeys[monkey].split(" ")
    match monkeys[monkey].split(" ")[1]:
        case "+":
            operation = operator.add
        case "-":
            operation = operator.sub
        case "*":
            operation = operator.mul
        case "/":
            operation = (operator.truediv)  # floordiv would be best, but sympy doesn't support it
    return operation(calc_monkey_val(m1, monkeys), calc_monkey_val(m2, monkeys))


if __name__ == "__main__":
    input_path = "./day_21/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
