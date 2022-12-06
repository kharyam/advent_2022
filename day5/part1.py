#!/usr/bin/python
import re

state={}
answer = 0
move_regex=re.compile('move (\d+) from (\d+) to (\d+)')


def parse_line(line):
    count=0
    for i in range(0,len(line),4):
        value = line[i+1]
        if value != ' ':
            if not state.get(count):
                state[count]=[]
            state[count].append(value)
        count+=1

def process(line):
    match=move_regex.match(line)
    amount=int(match.group(1))
    source=int(match.group(2))-1
    dest=int(match.group(3))-1

    for x in range(0,amount):
        state[dest].insert(0,state[source][0])
        state[source]=state[source][1:]

    # print("===============")
    # print(line)
    # print(state)

with open("input.txt") as file:
    for line in file:
        if line.startswith('['):
            parse_line(line)
        elif line.startswith("move"):
            process(line)

answer=dict(sorted(state.items()))
for k,v in answer.items():
    print(v[0],end='')

