#!/usr/bin/python
import re

sensors = []
no_beacon2=[]
max_x = 0
max_y = 0
min_x = 0
min_y = 0
beacon_regex = re.compile('x=([-+]?\d+), y=([-+]?\d+)')
ROW=2000000

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


def set_no_beacon2(start, stop):
    y=ROW
    no_beacon2.append([start,stop])


def mark_no_beacon(sensor, d):

    sx = sensor['x']
    sy = sensor['y']
    minx = sx-d
    maxx = sx+d
    miny = sy-d
    maxy = sy+d

    y=ROW
    if y<=sy+d and y>=sy-d:
        delta=abs(y-sy)
        startx=sx-d+delta
        stopx=sx+d-delta
        set_no_beacon2(startx,stopx)


def compute_coverage(sensor):
    d = sensor_beacon_dist(sensor)
    mark_no_beacon(sensor, d)

load_map('input.txt')
for sensor in sensors:
    compute_coverage(sensor)

# Fix this so works with one minimize
def minimize():
    has_i=True
    i=0
    while has_i:
        has_j=True
        j=0
        while has_j:
            if j==i:
                j+=1
            if j>=len(no_beacon2)-1:
                has_j=False
                break
            a1=no_beacon2[i][0]
            a2=no_beacon2[i][1]
            b1=no_beacon2[j][0]
            b2=no_beacon2[j][1]
            # print(f'{no_beacon2[i]} -- {no_beacon2[j]} -- {i} {j}')
            # if ( (((a1>=b1 and a1<=b2) or (a2>=b1 and a2<=b2)) or ((b1>=a1 and b1<=a2) or (b2>=a1 and b2<=a2))) and i!=j  ):
            if (not (a2 < b1 or b2 < a1)) and i!=j:
                no_beacon2[i][0]=min(a1,a2,b1,b2)
                no_beacon2[i][1]=max(a1,a2,b1,b2)
                no_beacon2.pop(j)
                i=0
            else:
                j+=1
        i+=1
        if i>=len(no_beacon2):
            has_i=False


minimize()
print(no_beacon2)
answer=0
for x in no_beacon2:
    answer+=x[1] - x[0]
answer+=1

beaconsx=[]
for s in sensors:
    y=s['b']['y']
    if y==ROW and not s['b']['x'] in beaconsx :
        beaconsx.append(s['b']['x'])
        answer-=1

print(answer)
