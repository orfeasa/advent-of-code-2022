def part_one(filename: str) -> int:
    moves = parse_input(filename)
    tail = head = (0, 0)
    tail_visited = {tail}
    for d, v in moves:
        for _ in range(v):
            dx, dy = move_knot(d)
            head = (head[0] + dx, head[1] + dy)
            tail = adjust_tail(tail, head)
            tail_visited.add(tail)
    return len(tail_visited)


def part_two(filename: str) -> int:
    moves = parse_input(filename)
    knots = [(0, 0) for _ in range(10)]
    tail_visited: set[tuple[int, int]] = set()
    for d, v in moves:
        for _ in range(v):
            dx, dy = move_knot(d)
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for i in range(1, len(knots)):
                knots[i] = adjust_tail(knots[i], knots[i - 1])
            tail_visited.add(knots[-1])
    return len(tail_visited)


def parse_input(filename: str) -> list[tuple[str, int]]:
    with open(filename, "r", encoding="utf8") as f:
        return [
            (d, int(v))
            for (d, v) in [tuple(line.strip().split()) for line in f.readlines()]
        ]


def move_knot(direction: str) -> tuple[int, int]:
    dir_to_move = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }
    return dir_to_move[direction]


def adjust_tail(tail: tuple[int, int], head: tuple[int, int]) -> tuple[int, int]:
    match head[0] - tail[0], head[1] - tail[1]:
        case _ as dx, _ as dy if abs(dx) <= 1 and abs(dy) <= 1:
            return (tail[0], tail[1])
        case 0, _ as dy:
            return (tail[0], tail[1] + dy // abs(dy))
        case _ as dx, 0:
            return (tail[0] + dx // abs(dx), tail[1])
        case dx, dy:
            return (tail[0] + dx // abs(dx), tail[1] + dy // abs(dy))


if __name__ == "__main__":
    input_path = "./day_09/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
