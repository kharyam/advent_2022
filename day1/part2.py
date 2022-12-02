#!/usr/bin/python

answers=[]
with open("input.txt") as file:
  total=0
  for line in file:
     if line == '\n':
       answers.append(total)
       total=0
     else:
       total+=int(line)

answers.sort(reverse=True)
answer = answers[0] + answers[1] + answers[2]
print(answer)


