import re

with open(r"input2.txt", "r", encoding= "utf-8") as file:
    #process data
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

truth = {'red': 12, 'green': 13, 'blue': 14}

def is_possible(game: dict, truth: dict) -> bool:
    """Returns a boolean value on whether or not a certain game is permissible
    given the total number of balls"""
    for color, number in game.items():
        if number > truth[color]:
            return False
    return True

id_sum = 0
for game_id, games in outcomes.items():
    game_count = 0
    for game in games:
        if not is_possible(game, truth):
            game_count += 1
    if game_count == 0:
        id_sum += game_id
print(id_sum)