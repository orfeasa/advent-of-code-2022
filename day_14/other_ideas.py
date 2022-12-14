def part_two_2(filename: str) -> int:
    rocks = parse_input(filename)
    y_max = max([y for _, y in rocks]) + 1
    sand = find_children((500, 0), y_max, rocks)
    return len(sand)


def find_children(
    curr_pos: tuple[int, int], y_max: int, rocks: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    if curr_pos[1] > y_max:
        return set()
    children = {curr_pos}
    for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
        next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
        if next_pos not in rocks:
            children |= find_children(next_pos, y_max, rocks)
    return children


def bfs(filename: str) -> int:
    rocks = parse_input(filename)
    y_max = max([y for _, y in rocks]) + 1
    sand = {(500, 0)}
    queue: Deque[tuple[int, int]] = deque([(500, 0)])
    while queue:
        curr_pos = queue.popleft()
        if curr_pos[1] >= y_max:
            continue
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
            if next_pos not in rocks:
                sand.add(next_pos)
                queue.append(next_pos)
    draw(rocks, sand)
    return len(sand)
