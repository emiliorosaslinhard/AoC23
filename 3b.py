
#rearrange text file into array
with open(r"input3.txt", "r", encoding= "utf-8") as file:
    engine = []
    for line in file:
        line = line.split("\n")
        engine.append([*line[0]])


def number_check(input_array, loc: tuple):
    """Given location of * in an array, finds if a number is adjacent,
    and if so, looks for another number, and if found, returns their product"""
    row, col = loc

    num_lst = []

    max_col = len(input_array[0])
    max_row = len(input_array)

    num_row = max_row + 1
    avoid_cols = [max_col + 1]

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if input_array[i][j].isdigit() and (i != num_row or j not in avoid_cols):
                num_row = i
                num, avoid_cols = find_complete_number(input_array, (i, j))
                num_lst.append(num)
                if len(num_lst) > 1:
                    break

    if len(num_lst) == 2:
        return num_lst[0] * num_lst[1]
    return 0


def find_complete_number(input_array, loc: tuple):
    """Given location of a single digit, return the complete number
    and the column of its locations"""
    num_lst = []
    col_lst = []
    row, col = loc
    max_col = len(input_array[0])

    #Look Right
    while col < max_col and input_array[row][col].isdigit():
        num_lst.append(input_array[row][col])
        col_lst.append(col)
        col += 1

    #Reset and look left
    col = loc[1] - 1

    #Look Left
    while col >= 0 and input_array[row][col].isdigit():
        num_lst.insert(0, input_array[row][col])
        col_lst.insert(0, col)
        col -= 1

    num =  int("".join(num_lst))
    print(num)
    return num, col_lst


total_sum = 0
for i, row in enumerate(engine):
    for j, _ in enumerate(row):
        if engine[i][j] == "*":
            total_sum += number_check(engine, (i, j))

print(total_sum)