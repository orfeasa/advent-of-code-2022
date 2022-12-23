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
    map_str, path_str = parse_input(filename)
    board, start = process_map(map_str)
    connect_nodes_flat(board)
    path = process_path(path_str)
    final_node, facing = follow_path(board, start, path)
    return 4 * final_node.x + 1000 * final_node.y + facing.value


def part_two(filename: str) -> int:
    return 0


def follow_path(
    board: dict[tuple[int, int], Node], start: tuple[int, int], path: list[int | str]
) -> tuple[Node, Direction]:
    current_node = board[start]
    facing = Direction.RIGHT
    visited = {start: facing}
    for step in path:
        if isinstance(step, int):
            for _ in range(step):
                visited[(current_node.x, current_node.y)] = facing
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
                    raise ValueError(f"Invalid rotation: '{step}'")
    return current_node, facing


def parse_input(filename: str) -> tuple[str, str]:
    with open(filename, encoding="utf8") as f:
        map_str, path_str = f.read().split("\n\n")
    return map_str, path_str


def process_map(
    map_str: str,
) -> tuple[dict[tuple[int, int], Node], tuple[int, int]]:
    board = {}
    start = 0, 0
    start_found = False
    for y, line in enumerate(map_str.split("\n"), 1):
        for x, char in enumerate(line, 1):
            if char == " ":
                continue
            if not start_found:
                start = x, y
                start_found = True
            board[(x, y)] = Node(value=char, x=x, y=y)
    return board, start


def connect_nodes_flat(board: dict[tuple[int, int], Node]) -> None:
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

    x_max, y_max = max(x for x, _ in board), max(y for _, y in board)
    for coord, node in board.items():
        node.left = find_next(board, coord, (-1, 0), x_max, y_max)
        node.right = find_next(board, coord, (1, 0), x_max, y_max)
        node.up = find_next(board, coord, (0, -1), x_max, y_max)
        node.down = find_next(board, coord, (0, 1), x_max, y_max)


def process_path(
    path_str: str,
) -> list[int | str]:
    path = []
    for step in re.split(r"(\d+)", path_str.strip()):
        if not step:
            continue
        if step.isdigit():
            path.append(int(step))
        else:
            path.append(step)
    return path


def print_map(
    board: dict[tuple[int, int], Node], visited: dict[tuple[int, int], Direction]
):
    x_max, y_max = max(x for x, _ in board), max(y for _, y in board)
    for y in range(1, y_max + 1):
        for x in range(1, x_max + 1):
            if (x, y) in visited:
                match visited[(x, y)]:
                    case Direction.RIGHT:
                        print(">", end="")
                    case Direction.DOWN:
                        print("v", end="")
                    case Direction.LEFT:
                        print("<", end="")
                    case Direction.UP:
                        print("^", end="")
            elif (x, y) in board:
                print(board[(x, y)].value, end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    input_path = "./day_22/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
