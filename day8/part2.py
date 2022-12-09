#!/usr/bin/python

tree_map=[]
answer=0

def check_vertical(x, y):
    vscore1=1
    vscore2=1
    for v in reversed(range(1,x)):
        if tree_map[v][y] < tree_map[x][y]:
            vscore1+=1
        else:
            break
    for v in range(x+1,len(tree_map)-1):
        if tree_map[v][y] < tree_map[x][y]:
            vscore2+=1
        else:
            break


    return (vscore1 * vscore2)

def check_horizontal(x, y):
    hscore1=1
    hscore2=1
    for h in reversed(range(1,y)):
        if tree_map[x][h] < tree_map[x][y]:
            hscore1+=1
        else:
            break

    for h in range(y+1,len(tree_map[0])-1):
        if tree_map[x][h] < tree_map[x][y]:
            hscore2+=1
        else:
            break

    return (hscore1 * hscore2)

def compute_score(x,y):
    return check_horizontal(x,y) * check_vertical(x,y)

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
        score=0
        if column==0 or column==width-1 or row==0 or row==height-1:
            score=0
        else:
            score = compute_score(x,y)
        if score>answer:
            answer = score

print(answer)
