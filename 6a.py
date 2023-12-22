import re

with open("input6.txt", "r", encoding="utf-8") as file:
    temp = []
    for line in file:
        _, game_data = re.split(r': ', line, maxsplit=1)
        temp.append(game_data.split())

races = {}
for i, item in enumerate(temp[0]):
    races[int(item)] = int(temp[1][i])

ways = 1
for time, distance in races.items():
    k = 0
    for i, _ in enumerate(range(time):
        if (time - i) * i > distance:
            k += 1
    ways *= k

print(ways)
