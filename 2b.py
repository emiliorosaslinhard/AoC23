import re

with open(r"input2.txt", "r", encoding= "utf-8") as file:
    outcomes = {}
    rp = r'(\d+)\s*red'
    bp = r'(\d+)\s*blue'
    gp = r'(\d+)\s*green'

    for line in file:
        id = int(re.search(r'\d+', line).group())

        long_str = re.split(r': ', line, maxsplit=1)

        games = []
        game_str = re.split(r'; ', long_str[1])
        for outcome in game_str:
            red_match = re.search(rp, outcome)
            red = int(red_match.group(1)) if red_match else 0

            green_match = re.search(gp, outcome)
            green = int(green_match.group(1)) if green_match else 0

            blue_match = re.search(bp, outcome)
            blue = int(blue_match.group(1)) if blue_match else 0

            occur = {'red': red, 'green': green, 'blue': blue}
            games.append(occur)

        outcomes[id] = games

def minimum_count(game_list) -> dict:
    """Given a list of dictionaries, finds a dictionary with the minimum
    possible value, then calculates the power"""
    minimum = {'red': 0, 'green': 0, 'blue':0}
    for game in game_list:
        for color, number in game.items():
            if number > minimum[color]:
                minimum[color] = number
    power = minimum['red'] * minimum['green'] * minimum['blue']
    return power

power_sum = 0
for game_list in outcomes.values():
    power_sum += minimum_count(game_list)

print(power_sum)