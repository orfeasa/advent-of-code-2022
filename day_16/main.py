import re


def part_one(filename: str) -> int:
    valve_flow, valve_tunnels = parse_input(filename)

    # starting with AA find all the paths and calculate the pressure released

    return 0


def part_two(filename: str) -> int:
    return 0


def dfs(graph: dict[str, set[str]], node: str, visited: set | None = None):
    visited = visited or set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


def total_pressure_released(
    valve: str, valve_flow: dict[str, int], now: int, end: int = 30
) -> int:
    return valve_flow[valve] * (end - now - 1)  # it takes a minute to open the valve


def calculate_distance(
    start: str,
    end: str,
    valve_tunnels: dict[str, set[str]],
) -> int:
    if dist := shortest_path(start, end, valve_tunnels):
        return len(dist)
    return 0


def shortest_path(
    start: str,
    end: str,
    valve_tunnels: dict[str, set[str]],
    path: list[str] | None = None,
) -> list[str] | None:
    path = path or []
    path += [start]
    if start == end:
        return path
    short_path = None
    for node in valve_tunnels[start]:
        if node not in path:
            if new_path := shortest_path(node, end, valve_tunnels, path):
                if not short_path or len(new_path) < len(short_path):
                    short_path = new_path
    return short_path


def parse_input(filename: str) -> tuple[dict[str, int], dict[str, set[str]]]:
    with open(filename, encoding="utf8") as f:
        lines = f.readlines()
    valve_flow = {
        line.split()[1]: int(line.split(";")[0].split("=")[-1]) for line in lines
    }
    valve_tunnels = {
        line.split()[1]: set(re.findall(r"[A-Z]+", line.split(";")[-1]))
        for line in lines
    }
    return valve_flow, valve_tunnels


if __name__ == "__main__":
    input_path = "./day_16/example1.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
