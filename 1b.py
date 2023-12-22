
"""Returns sum of two-digit pairs in puzzle input for part  of the December 1, 2023 """
#Dictionary to replace each text occurrence of a number with actual number
numbers = {"one": "on1e",
           "two": "tw2o",
           "three": "thre3e",
             "four": "fou4r",
             "five": "fiv5e",
             "six": "si6x",
             "seven": "seve7n",
             "eight": "eigh8t",
             "nine": "nin9e"}

with open(r"input.txt", "r", encoding="utf-8") as file:
    new_list = []
    for line in file:
        for number in numbers.items():
            count = line.count(number[0])
            line = line.replace(number[0], str(number[1]), count)
        new_list.append(line)


total_sum = 0
for string in new_list:
    forward = string
    reverse = string[::-1]

    tens = 0
    ones = 0


    for char in forward:
        if char.isdigit():
            tens = char
            break

    for char in reverse:
        if char.isdigit():
            ones = char
            break

    total_sum += int(tens) * 10 + int(ones)
print(total_sum)