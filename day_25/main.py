def part_one(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        numbers = {line.strip() for line in f.readlines()}
    return decimal_to_snafu(sum(snafu_to_decimal(number) for number in numbers))


def snafu_to_decimal(snafu: str) -> int:
    result = 0
    for digit in snafu:
        match digit:
            case "2":
                result = result * 5 + 2
            case "1":
                result = result * 5 + 1
            case "0":
                result = result * 5
            case "-":
                result = result * 5 - 1
            case "=":
                result = result * 5 - 2
    return result


def decimal_to_snafu(decimal: int) -> str:
    result = ""
    while decimal != 0:
        remainder = decimal % 5
        decimal = decimal // 5
        if remainder > 2:
            remainder -= 5
            decimal += 1
        match remainder:
            case 2:
                result = "2" + result
            case 1:
                result = "1" + result
            case 0:
                result = "0" + result
            case -1:
                result = "-" + result
            case -2:
                result = "=" + result
    return result


if __name__ == "__main__":
    input_path = "./day_25/input.txt"
    print("---Part One---")
    print(part_one(input_path))
