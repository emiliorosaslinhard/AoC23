import re

with open("input6.txt", "r", encoding="utf-8") as file:
    temp = []
    for line in file:
        _, game_data = re.split(r': ', line, maxsplit=1)
        temp.append(game_data.split())

time = int(''.join(temp[0]))
dist = int(''.join(temp[1]))

ways = 0
for i, _ in enumerate(range(time)):
    if (time - i) * i > dist:
        ways += 1
print(ways)

