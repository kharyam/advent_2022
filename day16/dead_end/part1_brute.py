#!/usr/bin/python
import re
FILE_NAME = "test.txt"
line_regex = re.compile('Valve (.+) has flow rate=(\d+).+valve[s]* (.*)$')
potential_valves = 0
leaves=[]

valves = {}
time = 30

def load_file(file_name):
    global potential_valves
    with open(file_name) as file:
        for line in file:
            matches = line_regex.findall(line)
            valves[matches[0][0]] = {"flow": int(
                matches[0][1]), "tunnels": matches[0][2].split(', ')}
            if (int(matches[0][1]) != 0):
                potential_valves += 1

def try_node(node):

    global leaves
    global potential_valves
    
    if (len(node['valves']) == potential_valves):
        leaves.append(node)
        return

    node['step']+=1
    step=node['step']
    if node['step'] == time:
        leaves.append(node)
        return

    if node['action']=='open':
       new_node={'name':node['name'], 'action':'move', 'parent':node, 'valves':node['valves'].copy(),'step':step,'children':[]}
       new_node['valves'].append(node['name'])
       node['children'].append(new_node)
       try_node(new_node)
       return
    for option in valves[node['name']]['tunnels']:
        new_node={'name':option, 'action':'move', 'parent':node, 'valves':node['valves'],'step':step,'children':[]}
        node['children'].append(new_node)
        try_node(new_node)
    if valves[node['name']]['flow'] >0 and valves[node['name']] not in node['valves']:
        new_node={'name':node['name'], 'action':'open', 'parent':node, 'valves':node['valves'],'step':step,'children':[]}
        node['children'].append(new_node)
        try_node(new_node)

def score_leaf(node):
    score=0
    count=0
    while node['parent']!=None:
        for valve in node['valves']:
            score+=valves[valve]['flow']
        node=node['parent']
    return score

load_file("test.txt")
root_node = {'name': 'AA', 'step': 0,
             'action': 'move', 'parent': None, 'valves': [], 'children':[]}

try_node(root_node)

winner={}
max_score=0

print(len(leaves))
for leaf in leaves:
    score=score_leaf(leaf)
    if score>max_score:
        max_score=score
        winner=leaf
print(max_score)
