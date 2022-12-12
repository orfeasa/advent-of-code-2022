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
                for dx in [-1, 1]
                for dy in [-1, 1]
                if 0 <= x + dx < len(line) and 0 <= y + dy < len(lines)
            ]
            for candidate in candidates:
                if (
                    abs(
                        get_elevation(char)
                        - get_elevation(lines[candidate[1]][candidate[0]])
                    )
                    <= 1
                ):
                    children.add(candidate)
            if children:
                graph[coord] = children
    visited = {start}
    dfs(visited, graph, start)
    return 0


def dfs(
    visited: set[tuple[int, int]],
    graph: dict[tuple[int, int], set[tuple[int, int]]],
    node: tuple[int, int],
):
    if node not in visited:
        visited.add(node)
        print(visited)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_12/example1.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
