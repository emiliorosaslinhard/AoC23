import re
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

def follow_instr(current, instr):
    """Given a dictionary entry and a direction, chooses the
    string corresponding to that entry"""
    if instr == 'L':
        return map_dict[current][0]
    return map_dict[current][1]

def part1(instructions):
    current = 'AAA'
    steps = 0
    instructions = cycle(instructions)
    instr = next(instructions)
    while current != 'ZZZ':
        current = follow_instr(current, instr)
        steps += 1
        instr = next(instructions)
    return steps




