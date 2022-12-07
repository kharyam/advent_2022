#!/usr/bin/python
import re

assignment_regex = re.compile('(\d+)-(\d+),(\d+)-(\d+)')
answer = 0


def range_contains(elf1_start, elf1_end, elf2_start, elf2_end):
    x = range(elf1_start, elf1_end+1)
    y = range(elf2_start, elf2_end+1)
    return any(c in x for c in y)


with open("input.txt") as file:
    for line in file:
        results = assignment_regex.match(line).groups()
        elf1_start = int(results[0])
        elf1_end = int(results[1])
        elf2_start = int(results[2])
        elf2_end = int(results[3])

        if range_contains(elf1_start, elf1_end, elf2_start, elf2_end):
            answer += 1

print(answer)
