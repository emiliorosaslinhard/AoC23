from operator import itemgetter
import re
import numpy as np

with open("input5.txt", "r", encoding="utf-8") as file:
    chunks = []
    current_chunk = []

    for line in file:
        if line.strip():
            current_chunk.append(line.strip())
        else:
            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = []

    if current_chunk:
        chunks.append("\n".join(current_chunk))

#dictionary
master = {}
for i, map in enumerate(chunks):
    if i == 0:
        master["seeds"] = [int(seed) for seed in map.split() if seed.isdigit()]
    else:
        map_name, value = re.split(r':\n', map, maxsplit=1)
        lines = []
        current_line = []
        current_num = ""

        for num in value:
            if num.isdigit():
                current_num += num
            elif num == " ":
                current_line.append(int(current_num))
                current_num = ""
            else:
                current_line.append(int(current_num))
                lines.append(current_line)
                current_num = ""
                current_line = []
        master[map_name] = np.array(lines)

def source_to_destination(array, source_num):
    sorted_array = sorted(array, key=lambda x: x[1])
    for line in sorted_array:
        if line[1] > source_num:
            break
        if line[1] <= source_num < line[1] + line[2]:
            return line[0] + source_num - line[1]
    return source_num

def seed_to_location(map_dict, seed_number):
    next_num = seed_number
    for map in map_dict.keys():
        if map != "seeds":
            next_num = source_to_destination(master[map], next_num)
        else:
            continue
    return next_num

locs = []
for seed in master["seeds"]:
    loc = seed_to_location(master, seed)
    locs.append(loc)

print(min(locs))
