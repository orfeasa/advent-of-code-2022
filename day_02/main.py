from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def to_move(move: str) -> Move:
    match move:
        case "A" | "X":
            return Move.ROCK
        case "B" | "Y":
            return Move.PAPER
        case "C" | "Z":
            return Move.SCISSORS
        case _:
            raise ValueError(f"Move {move} not recognised")


def part_one(filename: str) -> int:
    with open(filename) as f:
        moves = [tuple(line.split()) for line in f.readlines()]

    move_to_score = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    total_score = 0
    for move in moves:
        total_score += move_to_score[move[1]]
        total_score += calc_outcome_score(to_move(move[0]), to_move(move[1]))

    return total_score


def calc_outcome_score(opp_move, your_move: Move) -> int:
    match (opp_move, your_move):
        case (move1, move2) if move1 == move2:
            return 3
        case (Move.ROCK, Move.SCISSORS) | (Move.PAPER, Move.ROCK) | (
            Move.SCISSORS,
            Move.PAPER,
        ):
            return 0
        case (Move.SCISSORS, Move.ROCK) | (Move.ROCK, Move.PAPER) | (
            Move.PAPER,
            Move.SCISSORS,
        ):
            return 6
        case _:
            raise ValueError("Invalid moves")


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
