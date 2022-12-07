#!/usr/bin/python
import re

file_system = {}
current_directory = {}
file_regex = re.compile('(\d+) (.+)')
answer = 0
directory_sizes = []

with open("input.txt") as file:
    for line in file:
        if (line.startswith('$ cd /')):
            file_system['name'] = '/'
            file_system['parent'] = None
            file_system['directories'] = []
            file_system['files'] = []
            current_directory = file_system
        elif (line.startswith('$ cd ..')):
            mode = 'command'
            current_directory = current_directory['parent']
        elif (line.startswith('$ cd')):
            new_directory = {
                'name': line[5:], 'parent': current_directory,  'directories': [], 'files': []}
            current_directory['directories'].append(new_directory)
            current_directory = new_directory
        else:
            match = file_regex.match(line)
            if match:
                new_file = {'name': match.group(
                    2), 'size': int(match.group(1))}
                current_directory['files'].append(new_file)


def compute_size(directory):
    size = 0
    for file in directory['files']:
        size += file['size']
    for subdir in directory['directories']:
        size += compute_size(subdir)

    directory_sizes.append(size)
    return (size)


for directory in file_system['directories']:
    compute_size(directory)

for size in directory_sizes:
    if size <= 100000:
        answer += size

print(answer)
