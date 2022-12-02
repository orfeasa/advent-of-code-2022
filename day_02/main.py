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

    def move_score(self) -> int:
        match self:
            case Move.ROCK:
                return 1
            case Move.PAPER:
                return 2
            case Move.SCISSORS:
                return 3

    @classmethod
    def to_move(cls, move: str):
        match move:
            case "A" | "X":
                return Move.ROCK
            case "B" | "Y":
                return Move.PAPER
            case "C" | "Z":
                return Move.SCISSORS


def calc_outcome_score(opp_move, my_move: Move) -> int:
    match (opp_move, my_move):
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

    total_score = 0
    for move in moves:
        opp_move, my_move = Move.to_move(move[0]), Move.to_move(move[1])
        total_score += my_move.move_score()
        total_score += calc_outcome_score(opp_move, my_move)

    return total_score



def part_two(filename: str) -> int:
    with open(filename) as f:
        moves = [tuple(line.split()) for line in f.readlines()]
    total_score = 0
    for move, outcome in moves:
        opp_move = Move.to_move(move)
        match outcome:
            case "X": # lose
                my_move = opp_move.beats()
            case "Y": # draw
                my_move = opp_move
            case "Z": # win
                my_move = opp_move.loses_by()
        total_score += my_move.move_score()
        total_score += calc_outcome_score(opp_move, my_move)
    return total_score


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
