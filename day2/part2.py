#!/usr/bin/python

answer = 0
my_points = {"X": 1, "Y": 2, "Z": 3}

t = {"X": "ROCK", "A": "ROCK", "Y": "PAPER",
     "B": "PAPER", "Z": "SCISSORS", "C": "SCISSORS"}


def round_results(them, me):
    if t[them] == t[me]:
        return 3
    if (t[me] == "ROCK" and t[them] == "SCISSORS") or (t[me] == "PAPER" and t[them] == "ROCK") or (t[me] == "SCISSORS" and t[them] == "PAPER"):
        return 6
    else:
        return 0


with open("input.txt") as file:
    for line in file:
        their_move = t[line[0]]
        outcome = line[2]

        my_move = "Z"

        if (their_move == "ROCK" and outcome == "Y") or (their_move == "PAPER" and outcome == "X") or (their_move == "SCISSORS" and outcome == "Z"):
            my_move = "X"

        if (their_move == "ROCK" and outcome == "Z") or (their_move == "PAPER" and outcome == "Y") or (their_move == "SCISSORS" and outcome == "X"):
            my_move = "Y"

        answer += my_points[my_move] + round_results(line[0], my_move)


print(answer)
