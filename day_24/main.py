def part_one(filename: str) -> int:
    parse_input(filename)
    return 0


def part_two(filename: str) -> int:
    return 0


# parse input file in the form
# #.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#
def parse_input(filename: str) -> list:
    with open(filename, encoding="utf8") as f:
        valley_map = [line.strip() for line in f.readlines()]

    winds = {}
    for y, line in enumerate(valley_map):
        for x, char in enumerate(line):
            if char in "v^><":
                winds[(x, y)] = char
    start = (valley_map[0].find("."), 0)
    end = (valley_map[-1].find("."), len(valley_map) - 1)


if __name__ == "__ma5
n__":
    input_path = "./day_24/example2.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
