class InvalidGame(Exception):
    # Used kind of as a "super" break in the nested for loop
    pass

colors = {'red': 12, 'green': 13, 'blue': 14}

with open('./input') as games_file:
    games = []
    for game in games_file.readlines():
        games.append([])
        for round in game[:-1].split(':')[1].split(';'):
            games[-1].append({})
            for pull in round.split(','):
                games[-1][-1][pull.split(' ')[2]] = int(pull.split(' ')[1])
            for color in colors.keys():
                if color not in games[-1][-1].keys():
                    games[-1][-1][color] = 0
    # actual game
    sucess = 0
    for index, game in enumerate(games):
        try:
            for round in game:
                    for color, color_max in colors.items():
                        if round[color] > color_max: raise InvalidGame
        except InvalidGame:
            continue
        sucess += index + 1
    print(sucess)