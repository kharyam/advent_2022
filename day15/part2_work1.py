#!/usr/bin/python
import re

sensors = []
max_x = 0
max_y = 0
min_x = 0
min_y = 0
beacon_regex = re.compile('x=([-+]?\d+), y=([-+]?\d+)')
# ROW=20
ROW=4000000

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


def set_no_beacon(start, stop, row, answer_list):
    answer_list.append([start,stop])

def mark_no_beacon(sensor, d, y ,answer_list):

    sx = sensor['x']
    sy = sensor['y']
    minx = sx-d
    maxx = sx+d
    miny = sy-d
    maxy = sy+d

    if y<=sy+d and y>=sy-d:
        delta=abs(y-sy)
        startx=max(0,sx-d+delta)
        stopx=min(sx+d-delta,ROW)
        set_no_beacon(startx,stopx,y,answer_list)


def minimize(ranges):
    has_i=True
    i=0
    while has_i:
        has_j=True
        j=0
        while has_j:
            if j==i:
                j+=1
            if j>=len(ranges)-1:
                has_j=False
                break
            a1=ranges[i][0]
            a2=ranges[i][1]
            b1=ranges[j][0]
            b2=ranges[j][1]
            # print(f'{ranges[i]} -- {ranges[j]} -- {i} {j}')
            # if ( (((a1>=b1 and a1<=b2) or (a2>=b1 and a2<=b2)) or ((b1>=a1 and b1<=a2) or (b2>=a1 and b2<=a2))) and i!=j  ):
            if (not (a2 < b1 or b2 < a1)) and i!=j:
                ranges[i][0]=min(a1,a2,b1,b2)
                ranges[i][1]=max(a1,a2,b1,b2)
                ranges.pop(j)
                i=0
            else:
                j+=1
        i+=1
        if i>=len(ranges):
            has_i=False

def compute_coverage(sensor, row, answer_list):
    d = sensor_beacon_dist(sensor)
    mark_no_beacon(sensor, d, row, answer_list)


def print_row(answers):

    for i in range(0,20):
        found=False
        for a in answers:
            if i>=a[0] and i<=a[1]:
                print("#",end='')
                found=True
                break
        if not found:
            print(".",end='')
    print()
load_map('input.txt')

answer=[]
y=0
for i in range(ROW):
    answers=[]
    # sensors_row=[]
    for idx, sensor in enumerate(sensors):
        compute_coverage(sensor, i, answers)
        minimize(answers)
        # if(idx==11):
        #     t=[]
        #     compute_coverage(sensor, i, t)
        # sensors_row+=answers
        if len(answers)==2 and abs(answers[0][1]-answers[1][0]) == 2:
            answer=answers
            x=answer[0][1]+1
            y=i
            print(f'{x},{y} - {x*4000000+y}')
            # break
    if i%100000==0:
        print(i)
    # minimize(sensors_row)
    # print_row(sensors_row)
    

print(answer)
x=answer[0][1]+1
print(x)
print(y)
print(x*4000000+y)


# answer=0
# for x in answers:
#     answer+=x[1] - x[0]
# answer+=1

# beaconsx=[]
# for s in sensors:
#     y=s['b']['y']
#     if y==ROW and not s['b']['x'] in beaconsx :
#         beaconsx.append(s['b']['x'])
#         answer-=1

# print(answer)
