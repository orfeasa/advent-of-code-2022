def part_one(filename: str) -> int:
    with open(filename, encoding="utf8") as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    visible: set[tuple[int, int]] = set()
    x_max, y_max = len(nums[0]), len(nums)
    visible.update(
        *(
            [find_visible_in_line(nums, 0, x_max, y, y) for y in range(y_max)]
            + [find_visible_in_line(nums, x_max, 0, y, y) for y in range(y_max)]
            + [find_visible_in_line(nums, x, x, 0, y_max) for x in range(x_max)]
            + [find_visible_in_line(nums, x, x, y_max, 0) for x in range(x_max)]
        )
    )

    return len(visible)


def part_two(filename: str) -> int:
    return 0


def find_visible_in_line(
    nums: list[list[int]], x_min, x_max, y_min, y_max: int
) -> set[tuple[int, int]]:
    if x_min != x_max and y_min != y_max:
        raise ValueError(
            "x_min and x_max must be equal or y_min and y_max must be equal"
        )
    visible = set()
    current_max = 0
    if x_min == x_max:
        for y in range(y_min, y_max):
            if nums[y][x_min] > current_max:
                current_max = nums[y][x_min]
                visible.add((x_min, y))
    else:
        for x in range(x_min, x_max):
            if nums[y_min][x] > current_max:
                current_max = nums[y_min][x]
                visible.add((x, y_min))
    return visible


if __name__ == "__main__":
    input_path = "./day_08/example1.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
