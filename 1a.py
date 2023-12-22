
"""Returns sum of two-digit pairs in puzzle input for part 1 of the December 1, 2023 AoC challenge """
with open(r"input.txt", "r", encoding="utf-8") as file:
    total_sum = 0
    for line in file:
        forward = line
        reverse = line[::-1]

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
