#!/usr/bin/python
import ast


def get_list(line):
    return ast.literal_eval(line.strip())


def compare_lists(left, right):
    i = 0
    if len(right) == 0 and len(left) == 0:
        return None
    if len(left) == 0:
        return True
    if len(right) == 0 and len(left) > 0:
        return False

    while True:
        if i >= len(left):
            return True
        if i >= len(right):
            return False
        a = left[i]
        b = right[i]
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return True
            elif a > b:
                return False
            elif len(right) == 1 and len(left) == 1:
                return None
            i += 1
        elif isinstance(a, list) and isinstance(b, list):
            result = compare_lists(a, b)
            if result != None:
                return result
            i += 1
        else:
            if isinstance(a, int):
                a = [a]
            elif isinstance(b, int):
                b = [b]
            result = compare_lists(a, b)
            if result != None:
                return result
            i += 1


packets = []
with open("input.txt") as file:
    for line in file:
        if len(line) > 1:
            packets.append(get_list(line))
    packets.append([[2]])
    packets.append([[6]])

# Bubble Sort FTW
for i in range(len(packets)-1):
    for j in range(i+1, len(packets)):
        if compare_lists(packets[j], packets[i]):
            b = packets[i]
            packets[i] = packets[j]
            packets[j] = b

indexes = []
for idx, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        indexes.append(idx+1)

print(indexes[0] * indexes[1])
