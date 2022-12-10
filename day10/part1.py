#!/usr/bin/python

answer = 0
x=1
cycle=0
values=[x]
with open("input.txt") as file:
    for line in file:
        values.append(x)
        if line.startswith('noop'):
            cycle+=1
        else:
            amount=int(line[5:])
            values.append(x)
            cycle+=2
            x+=amount

for x in range(20,221,40):
    print(values[x])
    answer+=(x*values[x])

print(answer)
