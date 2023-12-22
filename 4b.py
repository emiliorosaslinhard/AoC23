import re

matches_dict = {}
with open("input4.txt", "r", encoding="utf-8") as file:
    for line in file:
        id = int(re.search(r'\d+', line).group())

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

        matches_dict[id] = k

def sum_counter(card, matches, matches_dict):
    iter = card
    copies = matches
    for i in range(matches):
        iter += 1
        copies += sum_counter(iter, matches_dict[iter], matches_dict)
    return copies

sum = 0
for card, matches in matches_dict.items():
    sum += 1 + sum_counter(card, matches, matches_dict)

print(sum)

