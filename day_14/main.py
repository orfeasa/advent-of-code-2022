def part_one(filename: str) -> int:
    rocks = parse_input(filename)

    y_max = max([y for _, y in rocks])
    sand = set()
    abyss = False
    count_sand = 0
    while not abyss:
        new_sand = (500, 0)
        curr_pos = new_sand
        rest = False
        while not rest:
            if curr_pos[1] > y_max:
                abyss = True
                break
            for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
                next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
                if next_pos not in rocks | sand:
                    curr_pos = next_pos
                    break
            else:
                rest = True
                count_sand += 1
                sand.add(curr_pos)
    return count_sand


def part_two(filename: str) -> int:
    rocks = parse_input(filename)

    y_max = max([y for _, y in rocks]) + 1
    sand = set()
    abyss = False
    count_sand = 0
    while not abyss:
        new_sand = (500, 0)
        curr_pos = new_sand
        rest = False
        while not rest:
            if curr_pos[1] >= y_max:
                rest = True
                count_sand += 1
                sand.add(curr_pos)
            for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
                next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
                if next_pos not in rocks | sand:
                    curr_pos = next_pos
                    break
            else:
                rest = True
                count_sand += 1
                sand.add(curr_pos)
                if curr_pos == new_sand:
                    abyss = True
                    break
    return count_sand


def parse_input(filename: str) -> set[tuple[int, int]]:
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()

    rocks = set()
    for line in lines:
        points = [
            tuple(map(int, coords.split(","))) for coords in line.strip().split(" -> ")
        ]
        for ind, point in enumerate(points[:-1:]):
            rocks.add(point)
            dx, dy = points[ind + 1][0] - point[0], points[ind + 1][1] - point[1]
            if dx:
                count = 0
                step = dx // abs(dx)
                while dx != count:
                    rocks.add((point[0] + count, point[1]))
                    count += step
            if dy:
                count = 0
                step = dy // abs(dy)
                while dy != count:
                    rocks.add((point[0], point[1] + count))
                    count += step
            rocks.add(points[ind + 1])
    return rocks


def draw(rocks, sand: set[tuple[int, int]]) -> None:
    y_min = min([y for _, y in rocks] + [y for _, y in sand])
    y_max = max([y for _, y in rocks] + [y for _, y in sand])
    x_min = min([x for x, _ in rocks] + [x for x, _ in sand])
    x_max = max([x for x, _ in rocks] + [x for x, _ in sand])
    for y in range(y_min - 1, y_max + 1):
        for x in range(x_min - 1, x_max + 1):
            if (x, y) in rocks:
                print("#", end="")
            elif (x, y) in sand:
                print("o", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    input_path = "./day_14/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
