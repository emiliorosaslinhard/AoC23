import re

total_points = 0
with open("input4.txt", "r", encoding="utf-8") as file:
    for line in file:

        _, game_data = re.split(r': ', line, maxsplit=1)
        winners_str, numbers_str = game_data.split('|')

        winner_ints = [int(num) for num in winners_str.split() if num.isdigit()]
        number_ints = [int(num) for num in numbers_str.split() if num.isdigit()]

        k = 0
        winner_list = []
        for number in number_ints:
            if number in winner_ints:
                winner_list.append(number)
                k += winner_ints.count(number)

        total_points += 2**(k-1) if k > 0 else 0
print(total_points)