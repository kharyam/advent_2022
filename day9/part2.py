#!/usr/bin/python

visits = {"0_0": 1}
num_tails = 9
tail_positions = {}

h = {'x': 0, 'y': 0}
for i in range(num_tails):
    tail_positions[i] = {'x': 0, 'y': 0}


# def print_state(h):
#     minx = 0
#     maxx = 0
#     miny = 0
#     maxy = 0

#     print(f'{tail_positions[4]["x"]},{tail_positions[4]["y"]}')

#     for i in tail_positions:
#         if tail_positions[i]['x'] < minx:
#             minx = tail_positions[i]['x']
#         if tail_positions[i]['x'] > maxx:
#             maxx = tail_positions[i]['x']
#         if tail_positions[i]['y'] < miny:
#             miny = tail_positions[i]['y']
#         if tail_positions[i]['y'] > maxy:
#             maxy = tail_positions[i]['y']
#     width = maxx-minx+2
#     height = maxy-miny+2

#     grid = []
#     for i in range(height):
#         grid.append([])
#         for j in range(width):
#             grid[i].append('.')

#     for i in reversed(range(len(tail_positions))):
#         grid[tail_positions[i]['y']][tail_positions[i]['x']] = f'{i+1}'

#     grid[h['y']][h['x']] = 'H'

#     for i in reversed(range(len(grid))):
#         for j in range(len(grid[i])):
#             print(grid[i][j], end='')
#         print()
#     print()


def compute_tail(t, h):
    deltax = h['x']-t['x']
    deltay = h['y']-t['y']

    if deltax == 2:
        t['x'] += 1
        if (deltay > 0):
            t['y'] += 1
        if (deltay < 0):
            t['y'] -= 1
    elif deltax == -2:
        t['x'] -= 1
        if (deltay > 0):
            t['y'] += 1
        if (deltay < 0):
            t['y'] -= 1
    elif deltay == 2:
        t['y'] += 1
        if (deltax > 0):
            t['x'] += 1
        if (deltax < 0):
            t['x'] -= 1
    elif deltay == -2:
        t['y'] -= 1
        if (deltax > 0):
            t['x'] += 1
        if (deltax < 0):
            t['x'] -= 1

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
            previous = h
            for j in range(len(tail_positions)):
                t = compute_tail(tail_positions[j], previous)
                tail_positions[j] = t
                previous = t
            visits[f'{tail_positions[8]["x"]}_{tail_positions[8]["y"]}'] = 1
            # print_state(h)

print(len(visits))
