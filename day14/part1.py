#!/usr/bin/python
import re

pair_regex = re.compile('(\d+,\d+)')
source = {'x': 500, 'y': 0}
lines = []
map = []
min_y = 0
max_y = 0
max_x = 0
min_x = -1
height = 0
width = 0


def load_file(file_name):
    global min_x
    global min_y
    global max_x
    global max_y
    global height
    global width

    with open(file_name) as file:
        for path in file:
            matches = pair_regex.findall(path)
            lines.append([])
            for match in matches:
                xy = match.split(',')
                x = int(xy[0])
                y = int(xy[1])
                if y > max_y:
                    max_y = y
                if x > max_x:
                    max_x = x
                if min_x == -1 or x < min_x:
                    min_x = x
                lines[-1].append({'x': x, 'y': y})
    height = max_y+1
    width = max_x-min_x+1


def build_map():
    for y in range(height):
        map.append([])
        for x in range(width):
            map[y].append('.')

    map[source['y']][source['x']-min_x] = '+'

    for line in lines:
        l = len(line)
        for idx, a in enumerate(line):
            if idx == l-1:
                break
            b = line[idx+1]
            if a['x'] != b['x']:
                startend = [a['x'], b['x']]
                startend.sort()
                for x in range(startend[0], startend[1]+1):
                    map[a['y']][x-min_x] = '#'

            elif a['y'] != b['y']:
                startend = [a['y'], b['y']]
                startend.sort()
                for y in range(startend[0], startend[1]+1):
                    map[y][a['x']-min_x] = '#'


def print_map():
    for y in range(height):
        for x in range(width):
            print(map[y][x], end='')
        print()


def simulate():

    unit = 0
    start = {'y': source['y'], 'x': source['x']-min_x}
    units_left = True
    while units_left:
        moves_left = True
        unit += 1
        c = start.copy()
        while moves_left:
            x = c['x']
            y = c['y']
            if y==max_y:
                units_left=False
                moves_left=False
            elif map[y+1][x] == '.':
                map[y+1][x] = 'o'
                map[y][x] = '.'
                c['y'] = y+1
            elif map[y+1][x-1] == '.':
                map[y+1][x-1] = 'o'
                map[y][x] = '.'
                c['y'] = y+1
                c['x'] = x-1
            elif map[y+1][x+1] == '.':
                map[y+1][x+1] = 'o'
                map[y][x] = '.'
                c['y'] = y+1
                c['x'] = x+1
            else:
                moves_left = False

            # print_map()
    print(unit-1)

load_file("input.txt")
build_map()
simulate()