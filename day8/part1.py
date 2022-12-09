#!/usr/bin/python

tree_map=[]
num_visible = 0

def check_vertical(x, y):
    vresult1=True
    vresult2=True
    for v in range(0,x):
        if tree_map[v][y] >= tree_map[x][y]:
            vresult1=False
            break

    for v in range(x+1,len(tree_map)):
        if tree_map[v][y] >= tree_map[x][y]:
            vresult2=False
            break
    return vresult1 or vresult2

def check_horizontal(x, y):
    hresult1=True
    hresult2=True
    for h in range(0,y):
        if tree_map[x][h] >= tree_map[x][y]:
            hresult1=False
            break

    for h in range(y+1,len(tree_map[0])):
        if tree_map[x][h] >= tree_map[x][y]:
            hresult2=False
            break
    return hresult1 or hresult2


with open("input.txt") as file:
    for index, line in enumerate(file):
        tree_map.append([])
        for n in line:
            if n != '\n':
                tree_map[index].append(int(n))

height=len(tree_map)
width=len(tree_map[0])


for column, x in enumerate(range(0,width)):
    for row, y in enumerate(range(0,height)):
        if column==0 or column==width-1 or row==0 or row==height-1:
            num_visible+=1
        elif check_vertical(x,y) or check_horizontal(x,y):
            num_visible+=1

print(num_visible)

