import numpy as np

line_count = 0
char_count = 0

#rearrange text file into array
with open(r"input3.txt", "r", encoding= "utf-8") as file:
    engine = []
    for line in file:
        line = line.split("\n")
        engine.append([*line[0]])


def number_check(input_array, loc: tuple):
    """Given location of number in an array, finds if symbols are adjacent,
    and if true, returns complete number, and if false, returns 0"""
    if not input_array[loc[0]][loc[1]].isdigit():
        return 0

    num_str = ""
    row, col = loc
    max_col = len(input_array[0])
    max_row = len(input_array)

    # Build the number from consecutive digits
    while col < max_col and input_array[row][col].isdigit():
        num_str += input_array[row][col]
        col += 1

    # Check adjacent cells for symbols
    for i in range(row - 1, row + 2):
        for j in range(col - len(num_str) - 1, col + 1):
            if 0 <= i < max_row and 0 <= j < max_col:
                if not input_array[i][j].isdigit() and input_array[i][j] != ".":
                    print (int(num_str))
                    return int(num_str)
    return 0

total_sum = 0
for i, row in enumerate(engine):
    for j, _ in enumerate(row):
        if (engine[i][j].isdigit() and (j == 0 or
            not engine[i][j-1].isdigit())):
            total_sum += number_check(engine, (i, j))

print(total_sum)