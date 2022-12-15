import re


def part_one(filename: str) -> int:
    sensors_beacons = parse_input(filename)
    sensors = {sb[0] for sb in sensors_beacons}
    beacons = {sb[1] for sb in sensors_beacons}
    xs = [s[0] for s in sensors] + [b[0] for b in beacons]
    ys = [s[1] for s in sensors] + [b[1] for b in beacons]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    sensors_dist = {(s[0][0], s[0][1]): manhattan(s[0], s[1]) for s in sensors_beacons}
    y = 2000000
    count = 0
    # draw(sensors,beacons,sensors_beacons)
    for x in range(x_min-1, x_max + 1):
        point = (x, y)
        if (
            is_point_covered(point, sensors_dist)
            and point not in sensors
            and point not in beacons
        ):
            print("#", end="")
            count += 1
        else:
            print(".", end="")
    return count


def part_two(filename: str) -> int:
    return 0


def is_point_covered(
    point: tuple[int, int], sensors_dist: dict[tuple[int, int], int]
) -> bool:
    for sensor, dist in sensors_dist.items():
        if manhattan(sensor, point) <= dist:
            return True
    return False


def manhattan(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_input(filename: str) -> list[list[tuple[int, int]]]:
    sensors = []
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            x1, y1, x2, y2 = map(int, re.findall(r"-?\d+", line))
            sensors.append([(x1, y1), (x2, y2)])
    return sensors


def draw(sensors, beacons: set[tuple[int,int]],sensors_beacons) -> None:
    xs = [s[0] for s in sensors] + [b[0] for b in beacons]
    ys = [s[1] for s in sensors] + [b[1] for b in beacons]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    sensors_dist = {(s[0][0], s[0][1]): manhattan(s[0], s[1]) for s in sensors_beacons}
    for y in range(y_min-10, y_max + 10):
        print(f"{y:02d} ", end="")
        for x in range(x_min - 10, x_max + 10):
            if (x, y) in sensors:
                print("S", end="")
            elif (x, y) in beacons:
                print("B", end="")
            elif is_point_covered((x,y), sensors_dist):
                print("#", end="")
            else:
                print(".", end="")
        print("")


if __name__ == "__main__":
    input_path = "./day_15/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
