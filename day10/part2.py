#!/usr/bin/python

answer = 0
x=1
cycle=0
values=[x]
crt=[]

def get_pixel():
    cycle_index=cycle%40
    if(cycle_index>=x-1 and cycle_index<=x+1):
        crt.append('#')
    else:
        crt.append('.')

with open("input.txt") as file:
    for line in file:
        values.append(x)
        if line.startswith('noop'):
            get_pixel()
            cycle+=1
        else:
            get_pixel()
            amount=int(line[5:])
            values.append(x)
            cycle+=1
            get_pixel()
            cycle+=1
            x+=amount
            
for i in range(len(crt)):
    if i%40==0:
        print()

    print(crt[i],end='')

