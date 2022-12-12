from dataclasses import dataclass


@dataclass
class Node:
    coord: tuple[int, int]
    children: set[tuple[int, int]]
    elevation: int

    @staticmethod
    def __repr__(self):
        return f"Node({self.coord}, {self.children})"


def get_elevation(elevation: str) -> int:
    if elevation == "S":
        return get_elevation("a")
    elif elevation == "E":
        return get_elevation("z")
    return ord(elevation) - ord("a")


def part_one(filename: str) -> int:
    start, end, graph = parse_input(filename)
    visited = bfs(graph, start)
    return visited[end]


def part_two(filename: str) -> int:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    start = end = (-1, -1)
    for y, line in enumerate(lines):
        if line.find("S") != -1:
            start = (line.find("S"), y)
        if line.find("E") != -1:
            end = (line.find("E"), y)
    start_candidates = {start}
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
                if (get_elevation(lines[y1][x1])-get_elevation(char) <= 1):
                    children.add((x1, y1))
            graph[coord] = children
            if char == "a":
                start_candidates.add(coord)

    steps_required = []
    for start in start_candidates:
        visited = bfs(graph, start)
        if end in visited:
            steps_required.append(visited[end])
    return min(steps_required)


def parse_input(filename: str) -> tuple[tuple[int, int], tuple[int, int], dict[tuple[int, int], set[tuple[int, int]]]]:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    start = end = (-1, -1)
    for y, line in enumerate(lines):
        if line.find("S") != -1:
            start = (line.find("S"), y)
        if line.find("E") != -1:
            end = (line.find("E"), y)

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
                if (get_elevation(lines[y1][x1])-get_elevation(char) <= 1):
                    children.add((x1, y1))
            graph[coord] = children
    return start, end, graph


def bfs(
    graph: dict[tuple[int, int], set[tuple[int, int]]],
    start: tuple[int, int],
):
    visited = {start: 0}
    steps = 0
    queue = [(start, steps)]
    while queue:
        s, steps = queue.pop(0)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited[neighbour] = steps + 1
                queue.append((neighbour, steps+1))
    return visited


if __name__ == "__main__":
    input_path = "./day_12/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
