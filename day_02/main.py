from enum import Enum, auto


class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

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
        raise ValueError("Invalid move")

    @classmethod
    def to_move(cls, move: str):
        match move:
            case "A" | "X":
                return Move.ROCK
            case "B" | "Y":
                return Move.PAPER
            case "C" | "Z":
                return Move.SCISSORS
        raise ValueError("Invalid move")


def calc_outcome_score(opp_move, my_move: Move) -> int:
    if opp_move == my_move:  # draw
        return 3
    if my_move == opp_move.loses_by():  # win
        return 6
    if my_move == opp_move.beats():  # lose
        return 0
    raise ValueError("Invalid moves")


def part_one(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        moves = [tuple(line.split()) for line in f.readlines()]

    total_score = 0
    for move in moves:
        opp_move, my_move = Move.to_move(move[0]), Move.to_move(move[1])
        total_score += my_move.move_score()
        total_score += calc_outcome_score(opp_move, my_move)

    return total_score


def part_two(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        moves = [tuple(line.split()) for line in f.readlines()]
    total_score = 0
    for move, outcome in moves:
        opp_move = Move.to_move(move)
        match outcome:
            case "X":  # lose
                my_move = opp_move.beats()
            case "Y":  # draw
                my_move = opp_move
            case "Z":  # win
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
