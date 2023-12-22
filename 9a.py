import re

lines = []
with open("input9.txt", "r", encoding="utf-8") as file:
    for line in file:
        nums = [int(num) if num.isdigit() or (num[0] == '-' and num[1:].isdigit()) else num for num in re.findall(r'-?\d+', line)]
        lines.append(nums)

def create_lists(num_list) -> list("list"):
    total = []
    working_list = num_list.copy()
    line_sum = sum(working_list)

    while any(num != 0 for num in working_list):
        total.insert(0, working_list)
        temp_list = []
        for i in range(len(working_list) - 1):
            temp_list.append(working_list[i + 1] - working_list[i])
        working_list = temp_list
    return total

def find_next_val(total_list, part=1):
    next_val = 0
    for i, num_list in enumerate(total_list[1:]):
        if part == 1:
            num_list.append(total_list[i][-1] + num_list[-1])
        elif part == 2:
            num_list.append(num_list[-1] - total_list[i][-1])
    next_val = total_list[-1][-1]
    return next_val


def part1(list_of_lists):
    grand_sum = 0
    for num_list in list_of_lists:
        triangle = create_lists(num_list)
        grand_sum += find_next_val(triangle)

    return grand_sum

def reverse_lists(triangle):
    new_list = []
    for old_list in triangle:
        old_list.reverse()
        new_list.append(old_list)
    return new_list


def part2(list_of_lists):
    grand_sum = 0
    for num_list in list_of_lists:
        triangle = create_lists(num_list)
        triangle_reversed = reverse_lists(triangle)
        grand_sum += find_next_val(triangle_reversed, 2)

    return grand_sum

#Answers
print("Part 1 Answer: ", part1(lines))
print("Part 2 Answer: ", part2(lines), "\n")
