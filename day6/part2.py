#!/usr/bin/python

marker_len = 14
with open("input.txt") as file:
    for line in file:
        for i in range(0, len(line)):
            potential_marker = line[i:i+marker_len]
            d = {}
            for j in potential_marker:
                d[j] = j
            if len(d.items()) == marker_len:
                print(i+marker_len)
                break
