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
        master["seeds"] = []
        prelim = [int(seed) for seed in map.split() if seed.isdigit()]
        for i in range(0, len(prelim), 2):
            master["seeds"].append((prelim[i], prelim[i + 1]))
        master["seeds"] = sorted(master["seeds"], key=lambda x: x[0])
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

def arrange_min(chunk):
    """arranges chunk into a list (including non given numbers)
    into an ascending order"""
    sorted_arrays = sorted(chunk, key=lambda x: x[1])

    #wow, turns out this is unnecessary because all arrays are neatly arranged
    #one after the other
    # constant_arrays = []
    # for i, range_array in enumerate(sorted_arrays[:-1]):
    #     if range_array[1] + range_array[2] == sorted_arrays[i + 1][1]:
    #         continue
    #     temp_start = range_array[1] + range_array[2]
    #     temp_range = sorted_arrays[i + 1][1] - temp_start
    #     temp_array = np.array((temp_start, temp_start, temp_range))
    #     index = i + 1 + len(constant_arrays)
    #     constant_arrays.append((index, temp_array))

    # for const_array in constant_arrays:
    #     sorted_arrays.insert(const_array[0], const_array[1])

    return sorted_arrays


#dest chunk ranges should only be the actual range, not include first number
def find_ranges_of_inputs(source_chunk, dest_chunk_ranges):
    """Given a range of outputs, find range (or ranges) of inputs responsible for
    generating that answer"""
    # sorted_source = sorted(source_chunk, key=lambda x: x[0])
    sorted_source = arrange_min(source_chunk)
    output_ranges = []
    for dest_range in dest_chunk_ranges:
        for source_range in sorted_source:
            #only consider overlapping regions
            if not (dest_range[0] + dest_range[1] < source_range[0] or
            source_range[0] + source_range[2] < dest_range[0]):
                new_min = source_range[1] + max(0, dest_range[0] - source_range[0])
                start_diff =  abs(dest_range[0] - source_range[0])
                #source range contained in dest range
                if (source_range[0] >= dest_range[0] and source_range[0] + source_range[2] <= dest_range[0] + dest_range[1]):
                    new_range = source_range[2]
                #dest range ccontained in source range
                elif (dest_range[0] >= source_range[0] and dest_range[0] + dest_range[1] <= source_range[0] + source_range[2]):
                    new_range = dest_range[1]

                #overlapped, source range first
                elif (source_range[0] < dest_range[0]):
                    new_range = source_range[2] - start_diff
                #overlapping, dest range first
                else:
                    new_range = dest_range[1] - start_diff
                output_ranges.append((new_min, new_range))
    return output_ranges

def find_seeds(sols_range):
    """Given a range of the last chunk, backtrack to find the ranges of seeds
    responsible"""
    range_input = sols_range
    for map in reversed(list(master.keys())[1:]):
        next_input = find_ranges_of_inputs(master[map], range_input)
        range_input = next_input
    return (range_input)

#very convenient fact about the input -> running through the first minimum array
#results in just one range of seeds, and the first number in that range corresponds
#to the minimum
last_chunks = arrange_min(master['humidity-to-location map'])
final_range = find_seeds([(last_chunks[0][1], last_chunks[0][2])])
seed_input = final_range[0][0]

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

final_number = seed_to_location(master, seed_input)
print("The answer you should submit is:", final_number)