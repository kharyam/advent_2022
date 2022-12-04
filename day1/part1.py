#!/usr/bin/python

answer = 0
with open("input.txt") as file:
    total = 0
    for line in file:
        if line == '\n':
            if total > answer:
                answer = total
            total = 0
        else:
            total += int(line)

print(answer)
