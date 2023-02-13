#!/usr/bin/python
import re

sensors = []
no_beacon = {}
max_x = 0
max_y = 0
min_x = 0
min_y = 0
beacon_regex = re.compile('x=([-+]?\d+), y=([-+]?\d+)')


def get_item(x, y):
    for sensor in sensors:
        if sensor['x'] == x and sensor['y'] == y:
            return 'S'
        if sensor['b']['x'] == x and sensor['b']['y'] == y:
            return 'B'
        if no_beacon.get(f'{x}_{y}'):
            return '#'

    return '.'


def set_minmax_x(x):
    global max_x
    global min_x
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x


def set_minmax_y(y):
    global max_y
    global min_y
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y


def set_no_beacon(x, y):
    global no_beacon
    if get_item(x, y) == '.':
        no_beacon[f'{x}_{y}'] = '#'
        set_minmax_x(x)
        set_minmax_y(y)


def print_map():
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            print(get_item(x, y), end='')
        print()


def load_map(file_name):
    global sensors
    global max_x
    global max_y
    with open(file_name) as file:
        for line in file:
            matches = beacon_regex.findall(line)
            sensor = {}

            sx = int(matches[0][0])
            sy = int(matches[0][1])
            bx = int(matches[1][0])
            by = int(matches[1][1])
            sensor['x'] = sx
            sensor['y'] = sy
            sensor['b'] = {}
            sensor['b']['x'] = bx
            sensor['b']['y'] = by

            set_minmax_x(sx)
            set_minmax_x(bx)
            set_minmax_y(sy)
            set_minmax_y(by)
            sensors.append(sensor)


def manhattan_distance(x1, y1, x2, y2):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return dx+dy


def sensor_beacon_dist(sensor):
    sx = sensor['x']
    sy = sensor['y']
    bx = sensor['b']['x']
    by = sensor['b']['y']

    return manhattan_distance(sx, sy, bx, by)


def mark_no_beacon(sensor, d):

    sx = sensor['x']
    sy = sensor['y']
    minx = sx-d
    maxx = sx+d
    miny = sy-d
    maxy = sy+d

    #for y in range(miny, maxy):
    y=2000000
    # for x in range(minx, maxx):
    if y<=sy+d and y>=sy-d:
        delta=abs(y-sy)
        startx=sx-d+delta
        stopx=sx+d-delta
        for x in range(startx,stopx):    
            if get_item(x, y) == '.' and manhattan_distance(sx, sy, x, y) <= d:
                set_no_beacon(x, y)


def no_beacon_count(y):
    count = 0
    for nb in no_beacon.items():
        if nb[0].endswith(f'_{y}'):
            count += 1
    return count


def compute_coverage(sensor):
    d = sensor_beacon_dist(sensor)
    mark_no_beacon(sensor, d)

load_map('input.txt')
count=1
for sensor in sensors:
    print(count)
    compute_coverage(sensor)
    count+=1

print_map()
print(no_beacon_count(2000000)+1)

