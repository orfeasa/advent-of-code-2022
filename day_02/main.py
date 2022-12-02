from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def beats(self):
        match self:
            case Move.ROCK:
                return Move.SCISSORS
            case Move.PAPER:
                return Move.ROCK
            case Move.SCISSORS:
                return Move.PAPER

    def loses_by(self):
        match self:
            case Move.ROCK:
                return Move.PAPER
            case Move.PAPER:
                return Move.SCISSORS
            case Move.SCISSORS:
                return Move.ROCK


    @classmethod
    def to_move(cls, move: str):
        match move:
            case "A" | "X":
                return cls.ROCK
            case "B" | "Y":
                return cls.PAPER
            case "C" | "Z":
                return cls.SCISSORS


def calc_outcome_score(opp_move, your_move: Move) -> int:
    match (opp_move, your_move):
        case (move1, move2) if move1 == move2:
            return 3
        case (move1, move2) if move2 == move1.beats():
            return 0
        case (move1, move2) if move2 == move1.loses_by():
            return 6
        case _:
            raise ValueError("Invalid moves")

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
        total_score += calc_outcome_score(Move.to_move(move[0]), Move.to_move(move[1]))

    return total_score



def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
