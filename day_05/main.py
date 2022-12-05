import re
from collections import defaultdict


def part_one(filename: str) -> str:
    stacks, instructions = parse_input(filename)
    stacks = process_instructions_9000(stacks, instructions)
    return get_stack_tops(stacks)


def part_two(filename: str) -> str:
    stacks, instructions = parse_input(filename)
    stacks = process_instructions_9001(stacks, instructions)
    return get_stack_tops(stacks)


def get_stack_tops(stacks: dict[int, list[str]]) -> str:
    tops = ""
    for ind in range(len(stacks)):
        tops += stacks[ind + 1][-1]
    return tops


def process_instructions_9000(
    stacks: dict[int, list[str]], instructions: list[list[int]]
) -> dict[int, list[str]]:
    for count, start, end in instructions:
        for _ in range(count):
            stacks[end].append(stacks[start].pop())
    return stacks


def process_instructions_9001(
    stacks: dict[int, list[str]], instructions: list[list[int]]
) -> dict[int, list[str]]:
    for count, start, end in instructions:
        for _ in range(count):
            tmp = stacks[start][-count:]
            stacks[end].extend(tmp)
            stacks[start] = stacks[start][:-count]
    return stacks


def parse_input(filename: str) -> tuple[dict[int, list[str]], list[list[int]]]:
    with open(filename, "r", encoding="utf8") as f:
        stacks_str, commands = f.read().split("\n\n")
    stacks_list = stacks_str.split("\n")
    stacks: dict[int, list[str]] = defaultdict(list)
    for stack in stacks_list[-2::-1]:
        stack_cursor = 0
        for column in range(0, len(stack), 4):
            current = stack[column : column + 3]
            if current != "   ":
                stacks[stack_cursor + 1].append(current.lstrip("[").rstrip("]"))
            stack_cursor += 1

    instructions = []
    for command in commands.strip().split("\n"):
        instructions.append(list(map(int, re.findall(r"\d+", command))))
    return stacks, instructions


if __name__ == "__main__":
    input_path = "./day_05/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
