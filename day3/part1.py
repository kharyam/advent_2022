#!/usr/bin/python

def priority(i):
    x = ord(i)
    if (x >= 97):
        return x-96
    return x-38


answer = 0
with open("input.txt") as file:
    for x in file:
        length = int(len(x)/2)
        first_half = x[0: length]
        second_half = x[length:]

        for c in first_half:
            if c in second_half:
                answer += priority(c)
                break

print(answer)
