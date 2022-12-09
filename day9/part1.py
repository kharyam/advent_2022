#!/usr/bin/python

visits = {"0_0": 1}
t = {'x': 0, 'y': 0}
h = {'x': 0, 'y': 0}


def compute_tail(t, h):
    deltax = h['x']-t['x']
    deltay = h['y']-t['y']

    if (deltax == 2 and deltay == 0):
        t['x'] += 1
    elif (deltax == -2 and deltay == 0):
        t['x'] -= 1
    elif (deltay == -2 and deltax == 0):
        t['y'] -= 1
    elif (deltay == 2 and deltax == 0):
        t['y'] += 1
    elif deltax == 2:
        t['x'] += 1
        t['y'] = h['y']
    elif deltax == -2:
        t['x'] -= 1
        t['y'] = h['y']
    elif deltay == 2:
        t['y'] += 1
        t['x'] = h['x']
    elif deltay == -2:
        t['y'] -= 1
        t['x'] = h['x']

    visits[f'{t["x"]}_{t["y"]}'] = 1
    return t


with open("input.txt") as file:
    for line in file:
        direction = line[0]
        steps = int(line[2:])
        for i in range(steps):
            if direction == "R":
                h['x'] += 1
            if direction == "L":
                h['x'] -= 1
            if direction == "U":
                h['y'] += 1
            if direction == "D":
                h['y'] -= 1
            t = compute_tail(t, h)

print(len(visits))
