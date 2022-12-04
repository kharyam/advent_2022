#!/usr/bin/python

def priority(i):
    x = ord(i)
    if (x >= 97):
        return x-96
    return x-38


answer = 0
file = open("input.txt")
lines = file.readlines()
current_line = 2

while current_line <= len(lines):
    for c in lines[current_line]:
        if c in lines[current_line - 1] and c in lines[current_line-2]:
            answer += priority(c)
            current_line += 3
            break

print(answer)
