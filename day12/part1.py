#!/usr/bin/python

el_map = []
visited_map = []
start = {}
end = {}
map_width = 0
map_height = 0
answers = []
backtrack={}

def read_map(file_name):
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            el_map.append(list(line))
            visited_map.append([0]*len(line))
            for idx, char in enumerate(line):
                x = idx
                y = len(el_map)-1
                if char == 'S':
                    start['x'] = x
                    start['y'] = y
                    el_map[y][x] = 'a'
                elif char == 'E':
                    end['x'] = x
                    end['y'] = y
                    el_map[y][x] = 'z'


def print_map():
    for y, line in enumerate(el_map):
        for x, el in enumerate(line):
            if (start['x'] == x and start['y'] == y):
                print('S', end='')
            elif (end['x'] == x and end['y'] == y):
                print('E', end='')
            else:
                print(el, end='')
        print()


def print_visited_map():
    for line in visited_map:
        for v in line:
            print(v, end='')
        print()


def get_height_coords(x, y):
    return ord(el_map[y][x])


def get_height(pos):
    return get_height_coords(pos['x'], pos['y'])


def visited(x, y):
    return visited_map[y][x] == 2 or visited_map[y][x] == 1


def mark_visited(x, y):
    visited_map[y][x] = 2


def mark_unvisited(x, y):
    visited_map[y][x] = 0


def mark_in_progress(x, y):
    visited_map[y][x] = 1


def set_backtrack(source, dest):
    backtrack[source['y']*map_width+source['x']] = dest['y']*map_width+dest['x']

def get_route(source):
    route=[]
    current=source['y']*map_width+source['x']
    done=False
    while not done:
        route.append(backtrack[current])
        current=backtrack[current]
        if current == backtrack[current]:
            done=True
    return route

def solve_map_steps(position):
    queue = []
    x = position['x']
    y = position['y']


    set_backtrack(position,position)
    mark_visited(x, y)
    queue.append(position)

    while not len(queue) == 0:
        pos = queue.pop(0)
        x = pos['x']
        y = pos['y']

        if x == end['x'] and y == end['y']:
            break
        else:
            height = get_height(pos)
            if x-1 >= 0 and not visited(x-1, y) and (get_height_coords(x-1, y) < height+2) :
                mark_visited(x-1, y)
                queue.append({'x': x-1, 'y': y})
                set_backtrack({'x': x-1, 'y': y},pos)
            if x+1 < map_width and not visited(x+1, y) and (get_height_coords(x+1, y) < height+2):
                mark_visited(x+1, y)
                queue.append({'x': x+1, 'y': y})
                set_backtrack({'x': x+1, 'y': y},pos)
            if y-1 >= 0 and not visited(x, y-1) and (get_height_coords(x, y-1) < height+2):
                mark_visited(x, y-1)
                queue.append({'x': x, 'y': y-1})
                set_backtrack({'x': x, 'y': y-1},pos)
            if y+1 < map_height and not visited(x, y+1) and (get_height_coords(x, y+1) < height+2):
                mark_visited(x, y+1)
                queue.append({'x': x, 'y': y+1})
                set_backtrack({'x': x, 'y': y+1},pos)
            mark_visited(x, y)


def solve_map(position):
    return solve_map_steps(position)


read_map('input.txt')
map_width = len(el_map[0])
map_height = len(el_map)

solve_map(start)
route = get_route(end)
print(len(route))
