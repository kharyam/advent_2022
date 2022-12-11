#!/usr/bin/python
import re

worry_operation = re.compile('(.+)\s(.+)')
commondenom=1

def compute_worry(monkey):
    worry = monkey['worry'][0]
    result = worry_operation.match(monkey['operation'])
    op = result.group(1)
    second = result.group(2)

    b = 0

    if (second == 'old'):
        b = worry
    else:
        b = int(second)

    if op == '+':
        return worry+b % commondenom
    elif op == '*':
        return worry*b % commondenom


monkeys = []
with open("input.txt") as file:
    for line in file:
        index = -1
        line = line.strip()
        if (line.startswith('Monkey')):
            index = int(line[7:].removesuffix(':'))
            monkeys.append({})
            monkeys[index]['inspected'] = 0
        elif (line.startswith("Starting items:")):
            monkeys[index]['worry'] = []
            items_str = line[16:].split(',')
            items = []
            for i in items_str:
                monkeys[index]['worry'].append(int(i.strip()))
        elif (line.startswith('Operation:')):
            monkeys[index]['operation'] = line[21:]
        elif (line.startswith('Test:')):
            monkeys[index]['test'] = int(line[19:])
            commondenom*=int(line[19:])
        elif (line.startswith('If true:')):
            monkeys[index]['true'] = int(line[25:])
        elif (line.startswith('If false:')):
            monkeys[index]['false'] = int(line[26:])

for round in range(0, 10000):
    for index, monkey in enumerate(monkeys):
        while len(monkey['worry']) != 0:
            monkey['inspected'] += 1
            worrylevel = compute_worry(monkey)
            if worrylevel % monkey['test'] == 0:
                monkeys[monkey['true']]['worry'].append(worrylevel)
            else:
                monkeys[monkey['false']]['worry'].append(worrylevel)
            del monkey['worry'][0]

inspections = []
for index, monkey in enumerate(monkeys):
    print(f'Monkey {index} inspected items {monkey["inspected"]} times.')
    inspections.append(monkey["inspected"])
s = sorted(inspections)
print(s.pop() * s.pop())
