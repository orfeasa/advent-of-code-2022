import operator


def part_one(filename: str) -> int:
    monkeys = parse_input(filename)
    return calc_monkey_val("root", monkeys)


def part_two(filename: str) -> int:
    return 0


def parse_input(filename: str) -> dict[str, int | str]:
    with open(filename, encoding="utf-8") as f:
        monkeys: dict[str, int | str] = {
            line.strip().split(": ")[0]: line.strip().split(": ")[1]
            for line in f.readlines()
        }
    for monkey in monkeys:
        if type(monkeys[monkey]) is str and len(monkeys[monkey].split(" ")) == 1:
            monkeys[monkey] = int(monkeys[monkey])
    return monkeys


def calc_monkey_val(monkey: str, monkeys: dict) -> int:
    if type(monkeys[monkey]) is int:
        return monkeys[monkey]

    m1, _, m2 = monkeys[monkey].split(" ")
    match monkeys[monkey].split(" ")[1]:
        case "+":
            oper = operator.add
        case "-":
            oper = operator.sub
        case "*":
            oper = operator.mul
        case "/":
            oper = operator.floordiv
    return oper(calc_monkey_val(m1, monkeys), calc_monkey_val(m2, monkeys))


if __name__ == "__main__":
    input_path = "./day_21/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
