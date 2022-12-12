from dataclasses import dataclass


@dataclass
class Node:
    coord: tuple[int, int]
    children: set[tuple[int, int]]
    elevation: int

    @staticmethod
    def get_elevation(elevation: str) -> int:
        if elevation == "S":
            return Node.get_elevation("a")
        elif elevation == "E":
            return Node.get_elevation("z")
        return ord(elevation) - ord("a")

    def __repr__(self):
        return f"Node({self.coord}, {self.children})"


def part_one(filename: str) -> int:
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    start = end = (-1, -1)
    for y, line in enumerate(lines):
        if line.find("S") != -1:
            start = (line.find("S"), y)
        if line.find("E") != -1:
            end = (line.find("E"), y)

    visited = {start}
    return 0


def dfs(visited: set[tuple[int, int]], graph, node: tuple[int, int]):
    if node not in visited:
        print(node)
        visited.add(node)
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
