def part_one(filename: str) -> int:
    register_values = process_input(filename)
    signal_sum = 0
    for s in [20, 60, 100, 140, 180, 220]:
        if s in register_values:
            signal_sum += s * register_values[s]
        elif s - 1 in register_values:
            signal_sum += s * register_values[s - 1]
        elif s - 2 in register_values:
            signal_sum += s * register_values[s - 2]

    return signal_sum


def part_two(filename: str) -> None:
    register_values = process_input(filename)
    drawn = []
    for position in range(240):
        cycle = position + 1
        register_val = get_register_value_at_cycle(register_values, cycle)
        if -1 <= position % 40 - register_val <= 1:
            drawn.append(position)
    draw(drawn)


def draw(drawn: list[int]) -> None:
    for y in range(6):
        for x in range(40):
            if x + y * 40 in drawn:
                print("#", end="")
            else:
                print(".", end="")
        print()


def get_register_value_at_cycle(register_values: dict[int, int], cycle: int) -> int:
    if cycle in register_values:
        return register_values[cycle]
    elif cycle - 1 in register_values:
        return register_values[cycle - 1]
    elif cycle - 2 in register_values:
        return register_values[cycle - 2]
    else:
        raise ValueError(f"Register value not found for {cycle=}")


def process_input(filename: str) -> dict[int, int]:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    x = 1
    cycles = 1
    register_values = {cycles: x}
    for line in lines:
        match line.split(" "):
            case ["noop"]:
                cycles += 1
            case ["addx", val]:
                cycles += 2
                x += int(val)
        register_values[cycles] = x
    return register_values


if __name__ == "__main__":
    input_path = "./day_10/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    part_two(input_path)
