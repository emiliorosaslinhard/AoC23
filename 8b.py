import re
import numpy as np
from itertools import cycle
map_dict = {}
directions = []


with open("input8.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file):
        if i == 0:
            instructions = [*line][:-1]
        elif i > 1:
            loc, direction = re.split(r' = ', line, maxsplit=1)
            intermed_dir = [*direction.strip()]
            left = "".join(intermed_dir[1:4])
            right = "".join(intermed_dir[6:9])
            map_dict[loc] = left, right

start_list = []
for loc in map_dict.keys():
    start = re.search('..A', loc)
    if start:
        start_list.append(loc)

def follow_instr(current, instr):
    """Given a dictionary entry and a direction, chooses the
    string corresponding to that entry"""
    if instr == 'L':
        return map_dict[current][0]
    return map_dict[current][1]

def part2(instructions, current):
    current = current
    steps = 0
    instructions = cycle(instructions)
    instr = next(instructions)
    while re.search('..Z', current) is None:
        current = follow_instr(current, instr)
        steps += 1
        instr = next(instructions)
    return steps

iter_list = []
for i, start in enumerate(start_list):
    iter_list.append(part2(instructions, start))

result = np.lcm.reduce(iter_list)
print(result)
