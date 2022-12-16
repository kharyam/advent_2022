#!/usr/bin/python
import re

pair_regex = re.compile('(\d+,\d+)')
source = {'x': 500, 'y': 0}
lines = []
map_dict = {}
min_y = 0
max_y = 0
max_x = 0
min_x = -1
height = 0
width = 0
floor = 0


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
                    map_dict[f'{x-min_x}_{a["y"]}'] = '#'

            elif a['y'] != b['y']:
                startend = [a['y'], b['y']]
                startend.sort()
                for y in range(startend[0], startend[1]+1):
                    map_dict[f'{a["x"]-min_x}_{y}'] = '#'


def get_map(x, y):
    key = f'{x}_{y}'

    if map_dict.get(key):
        return map_dict[key]
    elif y >= floor:
        map_dict[key] = '#'
        return ('#')
    else:
        map_dict[key] = '.'
        return ('.')


def set_map(x, y, str):
    key = f'{x}_{y}'
    map_dict[key] = str


def simulate():

    unit = 0
    units_left = True
    while units_left and get_map(source['x'], source['y']) != 'o':
        moves_remaining = True
        unit += 1
        c = source.copy()
        while moves_remaining:
            x = c['x']
            y = c['y']
            if y == floor:
                units_left = False
                moves_remaining = False
            elif get_map(x, y+1) == '.':
                set_map(x, y+1, 'o')
                set_map(x, y, '.')
                c['y'] = y+1
            elif get_map(x-1, y+1) == '.':
                set_map(x-1, y+1, 'o')
                set_map(x, y, '.')
                c['y'] = y+1
                c['x'] = x-1
            elif get_map(x+1, y+1) == '.':
                set_map(x+1, y+1, 'o')
                set_map(x, y, '.')
                c['y'] = y+1
                c['x'] = x+1
            else:
                set_map(x, y, 'o')
                moves_remaining = False

    print(unit)


load_file("input.txt")
floor = max_y+2

build_map()
source['x'] -= min_x
simulate()
