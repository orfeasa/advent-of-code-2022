def part_one(filename: str) -> int:
    with open(filename, encoding="utf8") as f:
        nums = list(map(lambda n: [int(x)
                    for x in list(n.strip())], f.readlines()))

    visible: set[tuple[int, int]] = set()
    x_max, y_max = len(nums[0]), len(nums)
    visible.update(
        *(
            [find_visible_in_line(nums, 0, x_max, y, y) for y in range(y_max)]
            + [find_visible_in_line(nums, x_max, 0, y, y)
               for y in range(y_max)]
            + [find_visible_in_line(nums, x, x, 0, y_max)
               for x in range(x_max)]
            + [find_visible_in_line(nums, x, x, y_max, 0)
               for x in range(x_max)]
        )
    )

    return len(visible)


def part_two(filename: str) -> int:
    with open(filename, encoding="utf8") as f:
        nums = list(map(lambda n: [int(x)
                    for x in list(n.strip())], f.readlines()))
    calculate_scenic_score(nums, 2, 1)
    # can't be on the edge
    max_score = 0
    x_max, y_max = len(nums[0]), len(nums)
    for y in range(1, y_max-1):
        for x in range(1, x_max-1):
            scenic_score = calculate_scenic_score(nums, x, y)
            if scenic_score > max_score:
                max_score = scenic_score
    return max_score


def calculate_scenic_score(
    nums: list[list[int]], x0: int, y0: int
) -> int:
    x_max, y_max = len(nums[0]), len(nums)
    val = nums[y0][x0]
    # count elements that are less than equal to the current element in each direction
    scenic_score = 1
    count_visible = 0
    for x in range(x0-1, -1, -1):
        count_visible += 1
        if nums[y0][x] >= val:
            break
    scenic_score *= count_visible

    count_visible = 0
    for x in range(x0+1, x_max):
        count_visible += 1
        if nums[y0][x] >= val:
            break
    scenic_score *= count_visible

    count_visible = 0
    for y in range(y0-1, -1, -1):
        count_visible += 1
        if nums[y][x0] >= val:
            break
    scenic_score *= count_visible

    count_visible = 0
    for y in range(y0+1, y_max):
        count_visible += 1
        if nums[y][x0] >= val:
            break
    scenic_score *= count_visible
    return scenic_score


def find_visible_in_line(
    nums: list[list[int]], x_min, x_max, y_min, y_max: int
) -> set[tuple[int, int]]:
    if x_min != x_max and y_min != y_max:
        raise ValueError(
            "x_min and x_max must be equal or y_min and y_max must be equal"
        )
    visible = set()
    current_max = -1
    if x_min == x_max:
        if y_min < y_max:
            for y in range(y_min, y_max):
                if nums[y][x_min] > current_max:
                    current_max = nums[y][x_min]
                    visible.add((x_min, y))
        else:
            for y in range(y_min-1, y_max-1, -1):
                if nums[y][x_min] > current_max:
                    current_max = nums[y][x_min]
                    visible.add((x_min, y))
    else:
        if x_min < x_max:
            for x in range(x_min, x_max):
                if nums[y_min][x] > current_max:
                    current_max = nums[y_min][x]
                    visible.add((x, y_min))
        else:
            for x in range(x_min-1, x_max-1, -1):
                if nums[y_min][x] > current_max:
                    current_max = nums[y_min][x]
                    visible.add((x, y_min))
    return visible


if __name__ == "__main__":
    input_path = "./day_08/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
