def part_one(filename: str) -> int:
    blizzards_start, start, end, x_max, y_max = parse_input(filename)
    return steps_to_end(start, end, blizzards_start, x_max, y_max)


def part_two(filename: str) -> int:
    blizzards_start, start, end, x_max, y_max = parse_input(filename)
    return steps_to_end(
        start,
        end,
        blizzards_start,
        x_max,
        y_max,
        steps_to_end(
            end,
            start,
            blizzards_start,
            x_max,
            y_max,
            steps_to_end(start, end, blizzards_start, x_max, y_max),
        ),
    )


def steps_to_end(
    start: tuple[int, int],
    end: tuple[int, int],
    blizzards_start: dict[tuple[int, int], str],
    x_max: int,
    y_max: int,
    t_start: int = 0,
) -> int:
    t = t_start
    curr_pos = {start}
    next_pos = set()
    while True:
        blizzards = get_blizzard_at_time(t + 1, blizzards_start, x_max, y_max)
        while curr_pos:
            x, y = curr_pos.pop()
            if (x, y) == end:
                return t
            for x1, y1 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (
                    1 <= x1 <= x_max and 1 <= y1 <= y_max and (x1, y1) not in blizzards
                ) or (x1, y1) in {start, end}:
                    next_pos.add((x1, y1))
            next_pos.add((x, y))
        curr_pos = next_pos - blizzards
        next_pos = set()
        t += 1


def get_blizzard_at_time(
    time: int,
    blizzards_start: dict[tuple[int, int], str],
    x_max: int,
    y_max: int,
) -> set[tuple[int, int]]:
    blizzards = set()
    for coord, direction in blizzards_start.items():
        x0, y0 = coord
        match direction:
            case "v":
                blizzards.add((x0, (y0 + time - 1) % y_max + 1))
            case "^":
                blizzards.add((x0, (y0 - time - 1) % y_max + 1))
            case ">":
                blizzards.add(((x0 + time - 1) % x_max + 1, y0))
            case "<":
                blizzards.add(((x0 - time - 1) % x_max + 1, y0))
    return blizzards


def print_map(
    wind_locations: set[tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
    x_max: int,
    y_max: int,
    current: set[tuple[int, int]] | None = None,
):
    for y in range(y_max + 2):
        for x in range(x_max + 2):
            match (x, y):
                case (x, y) if current and (x, y) in current:
                    print("o", end="")
                case (x, y) if (x, y) == start or (x, y) == end:
                    print(".", end="")
                case (_, 0) | (0, _):
                    print("#", end="")
                case (x, y) if x == x_max + 1 or y == y_max + 1:
                    print("#", end="")
                case (x, y) if (x, y) in wind_locations:
                    print("X", end="")
                case _:
                    print(".", end="")
        print()
    print()


def parse_input(
    filename: str,
) -> tuple[dict[tuple[int, int], str], tuple[int, int], tuple[int, int], int, int]:
    with open(filename, encoding="utf8") as f:
        valley_map = [line.strip() for line in f.readlines()]

    winds = {}
    for y, line in enumerate(valley_map):
        for x, char in enumerate(line):
            if char in "v^><":
                winds[(x, y)] = char
    start = (valley_map[0].find("."), 0)
    end = (valley_map[-1].find("."), len(valley_map) - 1)
    x_max = len(valley_map[0]) - 2
    y_max = len(valley_map) - 2
    return winds, start, end, x_max, y_max


if __name__ == "__main__":
    input_path = "./day_24/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
