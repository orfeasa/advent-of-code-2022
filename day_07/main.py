from typing import Type


class Directory:
    def __init__(self, name: str, parent: Type["Directory"] | None = None):
        self.name = name
        self.parent = parent
        self.children: list[Directory | File] = []

    def add_child(self, child: Type["Directory"] | Type["File"]):
        self.children.append(child)

    def get_path(self) -> str:
        if self.parent is None:
            return self.name
        return f"{self.parent.get_path()}/{self.name}"

    def get_child(self, name: str) -> Type["Directory"] | Type["File"]:
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError(f"Child {name} not found")

    def total_size(self) -> int:
        return sum(
            child.total_size() if isinstance(child, Directory) else child.size
            for child in self.children
        )

    def __repr__(self):
        return f"{self.name} (dir)"


class File:
    def __init__(self, name: str, parent: Type["Directory"], size: int):
        self.name = name
        self.parent = parent
        self.size = size

    def get_path(self) -> str:
        return f"{self.parent.get_path()}/{self.name}"

    def __repr__(self):
        return f"{self.name} (file, size={self.size})"


def total_size_of_children(directory: Directory, threshold: int) -> int:
    total_size = 0
    for child in directory.children:
        if isinstance(child, Directory) and child.total_size() <= threshold:
            total_size += child.total_size()
            total_size += total_size_of_children(child, threshold)

    return total_size


def part_one(filename: str) -> int:
    root = parse_input(filename)
    return total_size_of_children(root, 100000)


def parse_input(filename: str) -> Directory:
    with open(filename, "r", encoding="utf8") as f:
        terminal_output = f.read().strip().split("\n")
    root = Directory("/")
    current_directory = root
    for line in terminal_output:
        match line.split():
            case ["$", "ls"]:
                continue
            case ["$", "cd", ".."]:
                current_directory = current_directory.parent
            case ["$", "cd", "/"]:
                current_directory = root
            case ["$", "cd", directory] if directory != "/":
                current_directory = current_directory.get_child(directory)
            case ["dir", directory]:
                current_directory.add_child(Directory(directory, current_directory))
            case [size, filename]:
                current_directory.add_child(File(filename, current_directory, size))

    return root


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_07/example1.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
