from collections import deque
from typing import Deque


def part_one(filename: str) -> int:
    lines = parse_input(filename)
    start, end = get_start_end(lines)
    graph = construct_graph(lines)
    return bfs(graph, start, end)


def part_two(filename: str) -> int:
    lines = parse_input(filename)
    start, end = get_start_end(lines)
    graph = construct_graph(lines)
    start_candidates = {(x, y) for x, y in graph if get_elevation(lines[y][x]) == 0}
    steps_required = []
    for start in start_candidates:
        steps = bfs(graph, start, end)
        if steps != -1:
            steps_required.append(steps)
    return min(steps_required)


def parse_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def get_start_end(lines: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    start = end = (-1, -1)
    for y, line in enumerate(lines):
        if line.find("S") != -1:
            start = (line.find("S"), y)
        if line.find("E") != -1:
            end = (line.find("E"), y)
    return start, end


def get_elevation(elevation: str) -> int:
    if elevation == "S":
        return get_elevation("a")
    elif elevation == "E":
        return get_elevation("z")
    return ord(elevation) - ord("a")


def construct_graph(lines: list[str]) -> dict[tuple[int, int], set[tuple[int, int]]]:
    graph = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coord = (x, y)
            children = set()
            candidates = [
                (x + dx, y + dy)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= x + dx < len(line) and 0 <= y + dy < len(lines)
            ]
            for x1, y1 in candidates:
                if get_elevation(lines[y1][x1]) - get_elevation(char) <= 1:
                    children.add((x1, y1))
            graph[coord] = children
    return graph


def bfs(
    graph: dict[tuple[int, int], set[tuple[int, int]]],
    start: tuple[int, int],
    end: tuple[int, int],
):
    visited = {start: 0}
    steps = 0
    queue: Deque[tuple[tuple[int, int], int]] = deque()
    queue.append((start, steps))
    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited[neighbour] = steps + 1
                queue.append((neighbour, steps + 1))
    return -1


if __name__ == "__main__":
    input_path = "./day_12/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
