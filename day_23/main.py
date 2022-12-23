from collections import Counter, deque
from dataclasses import dataclass


class Dir:
    N = (0, -1)
    S = (0, 1)
    E = (1, 0)
    W = (-1, 0)
    NE = (1, -1)
    NW = (-1, -1)
    SE = (1, 1)
    SW = (-1, 1)


@dataclass
class Elf:
    x: int
    y: int


def part_one(filename: str) -> int:
    elves = parse_input(filename)
    directions_to_consider = deque(
        [
            (Dir.N, Dir.NE, Dir.NW),
            (Dir.S, Dir.SE, Dir.SW),
            (Dir.W, Dir.NW, Dir.SW),
            (Dir.E, Dir.NE, Dir.SE),
        ]
    )
    for _ in range(10):
        play_round(elves, directions_to_consider)
    return count_empty_tiles(elves)


def part_two(filename: str) -> int:
    elves = parse_input(filename)
    directions_to_consider = deque(
        [
            (Dir.N, Dir.NE, Dir.NW),
            (Dir.S, Dir.SE, Dir.SW),
            (Dir.W, Dir.NW, Dir.SW),
            (Dir.E, Dir.NE, Dir.SE),
        ]
    )
    elves_moved = True
    rounds = 0
    while elves_moved:
        elves_moved = play_round(elves, directions_to_consider)
        rounds += 1
    return rounds


def play_round(
    elves: dict[tuple[int, int], Elf],
    directions_to_consider: deque[tuple[tuple[int, int], ...]],
):
    proposals: dict[tuple[int, int], tuple[int, int]] = {}
    for elf in elves.values():
        if are_positions_empty(
            elf, elves, Dir.N, Dir.S, Dir.E, Dir.W, Dir.NE, Dir.NW, Dir.SE, Dir.SW
        ):
            continue
        for directions in directions_to_consider:
            if are_positions_empty(elf, elves, *directions):
                proposals[(elf.x, elf.y)] = (
                    elf.x + directions[0][0],
                    elf.y + directions[0][1],
                )
                break
    elves_moved = False
    duplicate_cells: set[tuple[int, int]] = {
        item for item, count in Counter(proposals.values()).items() if count > 1
    }
    for origin, destination in proposals.items():
        if destination not in duplicate_cells:
            elves[destination] = Elf(*destination)
            del elves[origin]
            elves_moved = True

    directions_to_consider.rotate(-1)
    return elves_moved


def are_positions_empty(
    elf: Elf, elves: dict[tuple[int, int], Elf], *directions: tuple[int, int]
) -> bool:
    return all(
        not (elf.x + direction[0], elf.y + direction[1]) in elves
        for direction in directions
    )


def parse_input(filename: str) -> dict[tuple[int, int], Elf]:
    with open(filename, encoding="utf8") as f:
        return {
            (x, y): Elf(x, y)
            for y, line in enumerate(f.readlines())
            for x, value in enumerate(line.strip())
            if value == "#"
        }


def count_empty_tiles(elves: dict[tuple[int, int], Elf]) -> int:
    x_min, x_max = min(x for x, _ in elves), max(x for x, _ in elves)
    y_min, y_max = min(y for _, y in elves), max(y for _, y in elves)
    return (x_max - x_min + 1) * (y_max - y_min + 1) - len(elves)


def print_map(elves: dict[tuple[int, int], Elf]):
    x_min, x_max = min(x for x, _ in elves), max(x for x, _ in elves)
    y_min, y_max = min(y for _, y in elves), max(y for _, y in elves)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


if __name__ == "__main__":
    input_path = "./day_23/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
