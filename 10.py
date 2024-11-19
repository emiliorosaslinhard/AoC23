import numpy as np
import math

#READ IN CONTENTS, THEN SWITCHED TO LOADING
# # Read the text file
# with open('input10.txt', 'r') as f:
#     content = f.read()

# # Create a 2D NumPy array
# lines = content.split('\n')
# max_len = max(len(line) for line in lines)
# array_2d = np.array([list(line.ljust(max_len)) for line in lines])

# np.save('array_2d.npy', array_2d)

array_2d = np.load('array_2d.npy')
          
                   #N  S  W  E
directions = {"|": ("N", "S"),
              "-": ("E", "W"), 
              "L": ("N", "E"),
              "J": ("N", "W"), 
              "7": ("S", "W"), 
              "F": ("S", "E"),
              ".": (), 
              "S": ("N", "S", "W", "E")}
reverse_directions = {v: k for k, v in directions.items()}

def find_starting_tile():
    for i, row in enumerate(array_2d):
        for j, element in enumerate(row):
            if element == "S":
                S_row = i
                S_col = j
    return (S_row, S_col)


def find_next_tile(row, col, dir):
    possible_next = directions[array_2d[row][col]]
    list_possible_next = list(possible_next)

    if dir in list_possible_next:
        list_possible_next.remove(dir)

    next_dir = list_possible_next[0] if list_possible_next else None


    #Look North     
    if row > 0 and "S" in directions[array_2d[row - 1][col]] and dir != "N" and (next_dir == "N" or dir == "X"):
        return (row - 1, col, array_2d[row - 1][col], "S")
    #Look South
    elif row < (len(array_2d[0]) - 1) and "N" in directions[array_2d[row + 1][col]] and dir != "S" and (next_dir == "S" or dir == "X"):
        return (row + 1, col, array_2d[row + 1][col], "N")
    #Look West
    elif col > 0 and "E" in directions[array_2d[row][col - 1]] and dir != "W" and (next_dir == "W" or dir == "X"):
        return (row, col - 1, array_2d[row][col - 1], "E")
    #Look East
    elif col < (len(array_2d) - 1) and "W" in directions[array_2d[row][col + 1]] and dir != "E" and (next_dir == "E" or dir == "X"):
        return (row, col + 1, array_2d[row][col + 1], "W")


def traverse_grid():
    pipe_list = []
    row, col = find_starting_tile()
    pipe_list.append((row, col))
    dir = "X"
    row, col, next, dir = find_next_tile(row, col, dir)
    pipe_list.append((row, col))
    count = 1
    
    while next != "S":
        row, col, next, dir = find_next_tile(row, col, dir)
        pipe_list.append((row, col))
        count += 1
    
    #return (math.ceil(count/2))
    return pipe_list

actual_grid = traverse_grid()

def count_no_tiles(pipe_list):
    return (math.floor(len(pipe_list)/2))

#Part 1 Answer
#print(count_no_tiles(traverse_grid()))

#PART 2

# #function to print completed path
# def print_completed_path():
#     modified_array = array_2d.copy()

#     # Replace junk pieces with ground
#     for i, row in enumerate(array_2d):
#         for j, element in enumerate(row):
#             if (i, j) not in actual_grid:
#                 modified_array[i, j] = "."

#     # Save the modified array to a text file
#     output_path = "completed_path.txt"
#     with open(output_path, "w") as f:
#         for row in modified_array:
#             f.write("".join(row) + "\n")
            
#     print(f"Modified array saved to {output_path}")

#need to determine and change S tile
def does_s_count():
    start_row, start_col = actual_grid[0]
    first_dir = find_next_tile(start_row, start_col, 'X')[3]

    end_row, end_col = actual_grid[-2]
    second_dir_reverse = find_next_tile(end_row, end_col, 'X')[3]
    if second_dir_reverse == "N":
        second_dir = "S"
    elif second_dir_reverse == "E":
        second_dir = "W"
    elif second_dir_reverse == "S":
        second_dir = "N"
    elif second_dir_reverse == "W":
        second_dir = "E"

    new_S = reverse_directions.get((first_dir, second_dir))
    array_2d[start_row][start_col] = new_S

does_s_count()    

#checks if piece is surrounded by pipe, only then returns true
def look_around(pos):
    rows, cols = len(array_2d), len(array_2d[0])  
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] 

    for dr, dc in directions:
        row, col = pos
        found = False

        while 0 <= row < rows and 0 <= col < cols:  
            if (row, col) in actual_grid:
                found = True
                break
            row += dr
            col += dc

        if not found:  
            return False

    return True


#preselect potential pieces
def preselect_pieces():
    preselected = []
    for i, row in enumerate(array_2d):
        for j, element in enumerate(row):
            if (i, j) not in actual_grid and look_around((i,j)):
                preselected.append((i,j))
    return preselected

PRESELECTED = preselect_pieces()

###SEE PRESELECTED PIECES
# def print_preselected_pieces():
#     modified_array = array_2d.copy()

#     # Replace junk pieces with ground
#     for i, row in enumerate(array_2d):
#         for j, element in enumerate(row):
#             if (i, j) not in actual_grid:
#                 modified_array[i, j] = "."
#             if (i, j) in PRESELECTED:
#                 modified_array[i, j] = "\u25A0"


#     # Save the modified array to a text file
#     output_path = "preselected_path.txt"
#     with open(output_path, "w") as f:
#         for row in modified_array:
#             f.write("".join(row) + "\n")
            
#     print(f"Preselected array saved to {output_path}")

#don't even need to look in all directions, can just look rightwards and count how many vertical tiles there are 
#but need to make this faster
#and also need special rule for L7 and FJ
def look_right_to_determine(pos):
    #failsafe
    if pos in actual_grid:
        return False
    
    row, curr_col = pos
    tile_count = 0 
    curr_col += 1
    last_col = 0
    while curr_col < (len(array_2d[row])):
        if (array_2d[row, curr_col] in ("|", "J", "F", "7", "L") and (row, curr_col) in actual_grid):
            tile_count += 1
            if last_col > 0: 
                if array_2d[row, curr_col] == "J":
                    if array_2d[row, last_col] == "F":
                        tile_count -= 1
                elif array_2d[row, curr_col] == "7":
                    if array_2d[row, last_col] == "L":
                        tile_count -= 1
            last_col = curr_col 
        curr_col += 1
    return tile_count % 2 == 1

def count_tiles_in():
    in_list = []
    tiles_in = 0
    for pos in PRESELECTED:
        if look_right_to_determine(pos):
            in_list.append(pos)
            tiles_in += 1
    return (tiles_in, in_list)

TILES_IN, IN_LIST = count_tiles_in()

###PRINT TILES
# def print_tiles_in():
#     modified_array = array_2d.copy()

#     # Replace junk pieces with ground
#     for i, row in enumerate(array_2d):
#         for j, element in enumerate(row):
#             if (i, j) not in actual_grid:
#                 modified_array[i, j] = "."
#             if (i, j) in PRESELECTED:
#                 modified_array[i, j] = "\u25A0"
#             if (i, j) in IN_LIST:
#                 modified_array[i, j] = "\u25A1"

#     # Save the modified array to a text file
#     output_path = "in_list_path.txt"
#     with open(output_path, "w") as f:
#         for row in modified_array:
#             f.write("".join(row) + "\n")
            
#     print(f"in List array saved to {output_path}")

# Part 2 Answer
print(TILES_IN)

