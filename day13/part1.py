#!/usr/bin/python
import ast


def get_list(line):
    return ast.literal_eval(line.strip())


def compare_lists(left, right):
    print(f'- Compare {left} vs {right}')
    i = 0
    if len(right) == 0 and len(left) == 0:
        return None
    if len(left) == 0:
        print("  - Left side ran out of items, so inputs are in the right order")
        return True
    if len(right) == 0 and len(left) > 0:
        print("  - Right side ran out of items, so inputs are not in the right order")
        return False

    while True:
        if i >= len(left):
            print("  - Left side ran out of items, so inputs are in the right order")
            return True
        if i >= len(right):
            print("  - Right side ran out of items, so inputs are not in the right order")
            return False
        a = left[i]
        b = right[i]
        print(f'  - Compare {a} vs {b}')
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                print(f'- Left side is smaller, so inputs are in the right order')
                return True
            elif a > b:
                print(f'- Right side is smaller, so inputs are not in the right order')
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


packet_pairs = []
with open("input.txt") as file:
    for idx, line in enumerate(file):
        if idx % 3 == 0:
            packet_pairs.append([])
            packet_pairs[-1] = [get_list(line)]
        elif idx % 3 == 1:
            packet_pairs[-1].append(get_list(line))

answers = []
for index, pair in enumerate(packet_pairs):
    left = pair[0]
    right = pair[1]
    print(f'== PAIR {index+1} ==')
    if compare_lists(left, right):
        answers.append(index+1)
    print()
result = 0
for a in answers:
    result += a
print(result)
