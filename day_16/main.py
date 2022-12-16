import re
from collections import deque
from typing import Deque
from collections import defaultdict


def part_one(filename: str) -> int:
    valve_flow, valve_tunnels = parse_input(filename)
    path = ("AA",)
    path_to_valve: dict[tuple[str, ...], int] = defaultdict(int)
    path_to_time: dict[tuple[str, ...], int] = defaultdict(int)
    time = 0
    opened = set()
    while time <= 30:
        candidates = {
            valve for valve in valve_flow if valve_flow[valve] and valve not in opened
        }
        for next in candidates:
            curr = path[-1]
            path_to_valve[path + (next,)] = path_to_valve[
                path
            ] + total_pressure_released_with_travel(
                curr, next, valve_flow, valve_tunnels, time
            )
            path_to_time[path + (next,)] = path_to_valve[
                path
            ] + bfs(valve_tunnels, curr, next) + 1
    return max(path_to_valve.values())


def part_one_greedy(filename: str) -> int:
    valve_flow, valve_tunnels = parse_input(filename)

    # greedy algorithm
    curr = "AA"
    time = 0
    opened = set()
    total_released = 0
    while time <= 30:
        candidates = {
            valve for valve in valve_flow if valve_flow[valve] and valve not in opened
        }
        valve_lifetime_value = {
            valve: total_pressure_released_with_travel(
                curr, valve, valve_flow, valve_tunnels, time
            )
            for valve in candidates
        }
        if not valve_lifetime_value:
            break
        next_valve = max(valve_lifetime_value, key=valve_lifetime_value.get)
        time += bfs(valve_tunnels, curr, next_valve) + 1
        opened.add(next_valve)
        total_released += valve_lifetime_value[next_valve]
        print(
            f"Minute: {time}, Moving to: {next_valve}, Total released: {total_released}"
        )
        curr = next_valve

    return total_released


def part_two(filename: str) -> int:
    return 0


def dfs(graph: dict[str, set[str]], node: str, visited: set | None = None):
    visited = visited or set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


def total_pressure_released_with_travel(
    start: str,
    valve: str,
    valve_flow: dict[str, int],
    valve_tunnels: dict[str, set[str]],
    now: int,
    end: int = 30,
) -> int:
    time_to_open = bfs(valve_tunnels, start, valve) + 1
    if (time_open := end - now - time_to_open) > 0:
        return valve_flow[valve] * time_open
    return 0


def total_pressure_released(
    valve: str, valve_flow: dict[str, int], now: int, end: int = 30
) -> int:
    return valve_flow[valve] * (end - now - 1)  # it takes a minute to open the valve


def bfs(
    graph: dict[str, set[str]],
    start: str,
    end: str,
) -> int:
    visited = {start: 0}
    steps = 0
    queue: Deque[tuple[str, int]] = deque()
    queue.append((start, steps))
    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited[neighbour] = steps + 1
                queue.append((neighbour, steps + 1))
    raise ValueError("No path found")


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
