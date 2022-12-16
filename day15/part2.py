#!/usr/bin/python
import re

sensors = []
beacon_regex = re.compile('x=([-+]?\d+), y=([-+]?\d+)')

# FILE_NAME="test.txt"
# ROW=20

FILE_NAME="input.txt"
ROW=4000000

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

def sensor_covers(sensor,x,y):
    d=sensor_beacon_dist(sensor)
    if manhattan_distance(sensor['x'],sensor['y'],x,y)>d:
        return False
    return True


def uncovered(x,y):
    for sensor in sensors:
        if sensor_covers(sensor,x,y):
            return False
    return True

load_map(FILE_NAME)

# DUMB WAY, CHECK ALL POINTS
# for y in range(ROW):
#     for x in range(ROW):
#         i+=1
#         if uncovered(x,y):
#             print(f'({x},{y}) = {x * 4000000 + y}')
#             exit(0)
#     if i%1000000==0:
#         print(i)


for idx,sensor in enumerate(sensors):
    print(f'sensor {idx}')
    d=sensor_beacon_dist(sensor)+1
    cx=sensor['x']
    cy=sensor['y']

    dx=1
    dy=-1
    x=cx
    y=cy+d
    for i in range(d):
        if (0<=x<=ROW and 0<=y<=ROW):
            if uncovered(x,y):
                print(f'({x},{y}) = {x * 4000000 + y}')
                exit(0)
            x+=dx
            y+=dy

    dx=-1
    dy=-1
    x=cx
    y=cy+d
    for i in range(d):
        if (0<=x<=ROW and 0<=y<=ROW):
            if uncovered(x,y):
                print(f'({x},{y}) = {x * 4000000 + y}')
                exit(0)
            x+=dx
            y+=dy

    dx=-1
    dy=1
    x=cx+d
    y=cy-d
    for i in range(d):
        if (0<=x<=ROW and 0<=y<=ROW):
            if uncovered(x,y):
                print(f'({x},{y}) = {x * 4000000 + y}')
                exit(0)
            x+=dx
            y+=dy

    dx=1
    dy=1
    x=cx+d
    y=cy-d
    for i in range(d):
        if (0<=x<=ROW and 0<=y<=ROW):
            if uncovered(x,y):
                print(f'({x},{y}) = {x * 4000000 + y}')
                exit(0)
            x+=dx
            y+=dy
