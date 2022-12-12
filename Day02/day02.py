from enum import Enum

INPUT_FILE = "input.txt"

class Scores(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0

class SymbolScores(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class PlayerValues(Enum):
    X = "ROCK"
    Y = "PAPER"
    Z = "SCISSORS"

class OpponentValues(Enum):
    A = "ROCK"
    B = "PAPER"
    C = "SCISSORS"

class PlayResult(Enum):
    X = "LOSE"
    Y = "DRAW"
    Z = "WIN"

def get_player_choice(choice):
    return PlayerValues[choice] == PlayerValues.X, PlayerValues[choice] == PlayerValues.Y, PlayerValues[choice] == PlayerValues.Z

def get_opponent_choice(choice):
    return OpponentValues[choice] == OpponentValues.A, OpponentValues[choice] == OpponentValues.B, OpponentValues[choice] == OpponentValues.C

def part_one():

    with open(INPUT_FILE, "r") as fp:
        data = fp.readlines()

    plays = [d.replace("\n", '').split() for d in data]
    res = 0

    for p in plays:
        p_rock, p_paper, p_scissors = get_player_choice(p[1])
        o_rock, o_paper, o_scissors = get_opponent_choice(p[0])
        res += (p_rock * o_rock * Scores.DRAW.value) + (p_rock * o_scissors * Scores.WIN.value) +\
               (p_paper * o_paper * Scores.DRAW.value) + (p_paper * o_rock * Scores.WIN.value) +\
               (p_scissors * o_scissors * Scores.DRAW.value) + (p_scissors * o_paper * Scores.WIN.value) +\
               (p_rock * SymbolScores["ROCK"].value) + (p_paper * SymbolScores["PAPER"].value) +\
               (p_scissors * SymbolScores["SCISSORS"].value)

    print(f"Result of part one: {res}")

def get_result_expected(res):
    return PlayResult[res] == PlayResult.Z, PlayResult[res] == PlayResult.Y, PlayResult[res] == PlayResult.X


def select_player_choice(opponent_play, play_result):
    o_rock, o_paper, o_scissors = get_opponent_choice(opponent_play)
    is_win, is_draw, is_loss = get_result_expected(play_result)

    p_rock = o_rock * is_draw + o_paper * is_loss + o_scissors * is_win
    p_paper = o_rock * is_win + o_paper * is_draw + o_scissors * is_loss
    p_scissors = o_rock * is_loss + o_paper * is_win + o_scissors * is_draw

    return p_rock, p_paper, p_scissors

def part_two():

    with open(INPUT_FILE, "r") as fp:
        data = fp.readlines()

    plays = [d.replace("\n", '').split() for d in data]
    res = 0

    for p in plays:
        p_rock, p_paper, p_scissors = select_player_choice(p[0], p[1])
        o_rock, o_paper, o_scissors = get_opponent_choice(p[0])
        res += (p_rock * o_rock * Scores.DRAW.value) + (p_rock * o_scissors * Scores.WIN.value) +\
               (p_paper * o_paper * Scores.DRAW.value) + (p_paper * o_rock * Scores.WIN.value) +\
               (p_scissors * o_scissors * Scores.DRAW.value) + (p_scissors * o_paper * Scores.WIN.value) +\
               (p_rock * SymbolScores["ROCK"].value) + (p_paper * SymbolScores["PAPER"].value) +\
               (p_scissors * SymbolScores["SCISSORS"].value)

    print(f"Result of part two: {res}")

if __name__ == '__main__':
    part_one()
    part_two()
