import copy


def part_one(filename: str) -> int:
    with open(filename, "r", encoding="utf8") as f:
        moves = [
            (d, int(v))
            for (d, v) in [tuple(line.strip().split()) for line in f.readlines()]
        ]
    tail = head = (0, 0)
    tail_visited = set()
    tail_visited.add(tail)
    for d, v in moves:
        for _ in range(v):
            match d:
                case "U":
                    head = (head[0], head[1] + 1)
                case "D":
                    head = (head[0], head[1] - 1)
                case "R":
                    head = (head[0] + 1, head[1])
                case "L":
                    head = (head[0] - 1, head[1])
            tail = adjust_tail(tail, head)
            tail_visited.add(tail)

    return len(tail_visited)


def adjust_tail(tail: tuple[int, int], head: tuple[int, int]) -> tuple[int, int]:
    new_tail = copy.deepcopy(tail)
    if new_tail[0] < head[0] - 1:
        new_tail = (new_tail[0] + 1, new_tail[1])
    if new_tail[0] > head[0] + 1:
        new_tail = (new_tail[0] - 1, new_tail[1])
    if new_tail[1] < head[1] - 1:
        new_tail = (new_tail[0], new_tail[1] + 1)
    if new_tail[1] > head[1] + 1:
        new_tail = (new_tail[0], new_tail[1] - 1)

    return new_tail


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_09/example1.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
