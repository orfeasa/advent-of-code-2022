def part_one(filename: str) -> int:
    cubes = parse_input(filename)
    return sum(
        [
            1
            for cube in cubes
            for d in [-1, 1]
            for dx, dy, dz in [(d, 0, 0), (0, d, 0), (0, 0, d)]
            if (cube[0] + dx, cube[1] + dy, cube[2] + dz) not in cubes
        ]
    )


def part_two(filename: str) -> int:
    cubes = parse_input(filename)
    exterior = 0
    for cube in cubes:
        for direction in [-1, 1]:
            for dir_x, dir_y, dir_z in [
                (direction, 0, 0),
                (0, direction, 0),
                (0, 0, direction),
            ]:
                is_exterior = True
                for res in range(1, 4):
                    dx, dy, dz = dir_x * res, dir_y * res, dir_z * res
                    if (cube[0] + dx, cube[1] + dy, cube[2] + dz) in cubes:
                        is_exterior = False
                        break
                if is_exterior:
                    exterior += 1
    return exterior


def parse_input(filename) -> set[tuple[int, ...]]:
    with open(filename, encoding="utf8") as f:
        return {tuple(map(int, line.strip().split(","))) for line in f.readlines()}


if __name__ == "__main__":
    input_path = "./day_18/example1.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
