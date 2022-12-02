#!/usr/bin/python

answer=0
my_points = { "X" : 1, "Y" : 2, "Z" : 3 }

t = {"X" : "ROCK", "A" : "ROCK", "Y" : "PAPER", "B" : "PAPER", "Z" : "SCISSORS", "C" : "SCISSORS"}


def round_results(them, me):
  if t[them] == t[me]:
    return 3
  if (t[me] == "ROCK" and t[them]=="SCISSORS" ) or (t[me] == "PAPER" and t[them]=="ROCK" ) or (t[me] == "SCISSORS" and t[them]=="PAPER" ):
    return 6
  else:
    return 0
  
with open("input.txt") as file:
  for line in file:
    answer += my_points[line[2]] + round_results(line[0],line[2]) 
    

print(answer)


