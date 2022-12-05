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

    for x in range(amount-1,-1,-1):
        state[dest].insert(0,state[source][x])
    state[source]=state[source][amount:]

    # print("===============")
    # print(line)
    # print(state)

with open("input.txt") as file:
    count=0
    stage=0
    for line in file:
        if stage==0 and not "1" in line:
            parse_line(line)
        elif stage==0 and "1" in line:
            stage=1
        elif line.startswith("move"):
            process(line)
        count+=1

answer=dict(sorted(state.items()))
for k,v in answer.items():
    print(v[0],end='')

