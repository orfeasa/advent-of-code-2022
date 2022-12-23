import re
from enum import Enum
from typing import Type


class Node:
    value: str
    x: int
    y: int
    left: Type["Node"] | None = None
    right: Type["Node"] | None = None
    up: Type["Node"] | None = None
    down: Type["Node"] | None = None

    def __init__(self, value: str, x: int, y: int):
        self.value = value
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Node({self.x}, {self.y})"


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    @classmethod
    def clockwise(cls, direction: "Direction") -> "Direction":
        return cls((direction.value + 1) % 4)

    @classmethod
    def counter_clockwise(cls, direction: "Direction") -> "Direction":
        return cls((direction.value - 1) % 4)


def part_one(filename: str) -> int:
    start, board, path = parse_input(filename)
    current_node = board[start]
    facing = Direction.RIGHT
    for step in path:
        if isinstance(step, int):
            for _ in range(step):
                match facing:
                    case Direction.RIGHT:
                        next_node = current_node.right
                    case Direction.DOWN:
                        next_node = current_node.down
                    case Direction.LEFT:
                        next_node = current_node.left
                    case Direction.UP:
                        next_node = current_node.up
                    case _:
                        raise ValueError(f"Invalid direction: {facing}")
                if next_node.value == "#":
                    break
                current_node = next_node
        else:
            match step:
                case "L":
                    facing = Direction.counter_clockwise(facing)
                case "R":
                    facing = Direction.clockwise(facing)
                case _:
                    raise ValueError(f"Invalid rotation: {step}")
    print(f"{current_node=}, {facing=}")
    return 4 * current_node.x + 1000 * current_node.y + facing.value


def part_two(filename: str) -> int:
    return 0


def parse_input(
    filename: str,
) -> tuple[tuple[int, int], dict[tuple[int, int], Node], list[int | str]]:
    with open(filename, encoding="utf8") as f:
        map_str, path_str = f.read().split("\n\n")

    board = {}
    x_max, y_max = 0, 0
    start = 0, 0
    start_found = False
    for y, line in enumerate(map_str.split("\n"), 1):
        y_max = max(y, y_max)
        for x, char in enumerate(line, 1):
            x_max = max(x, x_max)
            if char == " ":
                continue
            if not start_found:
                start = x, y
                start_found = True
            board[(x, y)] = Node(value=char, x=x, y=y)
    for coord, node in board.items():
        node.left = find_next(board, coord, (-1, 0), x_max, y_max)
        node.right = find_next(board, coord, (1, 0), x_max, y_max)
        node.up = find_next(board, coord, (0, -1), x_max, y_max)
        node.down = find_next(board, coord, (0, 1), x_max, y_max)

    path = [
        x
        for step in re.findall(r"\d+[A-Z]+", path_str)
        for x in [int(step[:-1]), step[-1]]
    ]

    return start, board, path


def find_next(
    board: dict[tuple[int, int], Node],
    coord: tuple[int, int],
    direction: tuple[int, int],
    x_max: int,
    y_max: int,
) -> Node:
    x, y = coord
    x_next, y_next = direction
    while (
        new_coord := ((x + x_next - 1) % x_max + 1, (y + y_next - 1) % y_max + 1)
    ) not in board:
        x_next += direction[0]
        y_next += direction[1]
    return board[new_coord]


def find_right(
    board: dict[tuple[int, int], Node], x: int, y: int, x_max, y_max
) -> Node:
    if x + 1 > x_max:
        return board[(1, y)]
    if (x + 1, y) in board:
        return board[(x + 1, y)]
    return find_right(board, x + 1, y, x_max, y_max)


def find_up(board: dict[tuple[int, int], Node], x: int, y: int, x_max, y_max) -> Node:
    if y - 1 < 1:
        return board[(x, y_max)]
    if (x, y - 1) in board:
        return board[(x, y - 1)]
    return find_up(board, x, y - 1, x_max, y_max)


def find_down(board: dict[tuple[int, int], Node], x: int, y: int, x_max, y_max) -> Node:
    if y + 1 > y_max:
        return board[(x, 1)]
    if (x, y + 1) in board:
        return board[(x, y + 1)]
    return find_down(board, x, y + 1, x_max, y_max)


if __name__ == "__main__":
    input_path = "./day_22/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
