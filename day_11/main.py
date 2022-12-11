from typing import Callable
import operator


class Monkey:
    id: int
    items: list[int]
    operation: Callable[[int, int], int]
    mod: int
    if_true: int
    if_false: int
    count_inspections: int

    def __init__(self, lines_str: str):
        lines = [line.strip() for line in lines_str.split("\n")]
        self.id = int(lines[0].split(" ")[1].strip(":"))
        self.items = [int(item) for item in lines[1].split(": ")[1].split(", ")]
        self.mod = int(lines[3].lstrip("Test: divisible by "))
        left, operand, right = lines[2].split(" = ")[-1].split(" ")
        match [left, operand, right]:
            case ["old", "+", "old"]:
                self.operator, self.operand = operator.mul, 2
            case ["old", "*", "old"]:
                self.operator, self.operand = operator.pow, 2
            case ["old", "+", _ as num]:
                self.operator, self.operand = operator.add, int(num)
            case ["old", "*", _ as num]:
                self.operator, self.operand = operator.mul, int(num)
        self.if_true = int(lines[4].split("monkey ")[1])
        self.if_false = int(lines[5].split("monkey ")[1])
        self.count_inspections = 0

    def __repr__(self) -> str:
        return f"Monkey {self.id}: {', '.join(str(item) for item in self.items)}"


def part_one(filename: str) -> int:
    monkeys = parse_input(filename)
    for _ in range(20):
        run_round(monkeys, 3)
    inspections = sorted([monkey.count_inspections for monkey in monkeys.values()])
    return inspections[-1] * inspections[-2]


def part_two(filename: str) -> int:
    monkeys = parse_input(filename)
    for _ in range(10000):
        run_round(monkeys, 1)
        if _ + 1 in [
            1,
            20,
            1000,
            2000,
            3000,
            4000,
            5000,
            6000,
            7000,
            8000,
            9000,
            10000,
        ]:
            print(f"\n== After round {_+1} ==")
            for monkey in monkeys.values():
                print(
                    f"Monkey {monkey.id}: inspected items {monkey.count_inspections} times."
                )
    inspections = sorted([monkey.count_inspections for monkey in monkeys.values()])
    return inspections[-1] * inspections[-2]


def run_round(monkeys: dict[int, "Monkey"], worry_divider=1) -> None:
    for monkey_id, _ in enumerate((monkeys)):
        monkey = monkeys[monkey_id]
        if len(monkey.items) == 0:
            continue
        monkey.count_inspections += len(monkey.items)
        for item in monkey.items:
            new = monkey.operator(item, monkey.operand) // worry_divider
            if new % monkey.mod == 0:
                monkeys[monkey.if_true].items.append(new)
            else:
                monkeys[monkey.if_false].items.append(new)
        monkey.items = []


def parse_input(filename: str) -> dict[int, Monkey]:
    with open(filename, "r", encoding="utf8") as f:
        monkeys_str = f.read().split("\n\n")
    monkeys_list = [Monkey(monkey_str) for monkey_str in monkeys_str]
    return {monkey.id: monkey for monkey in monkeys_list}


if __name__ == "__main__":
    input_path = "./day_11/example1.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
