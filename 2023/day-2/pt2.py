class InvalidGame(Exception):
    # Used kind of as a "super" break in the nested for loop
    pass

colors = {'red': 0, 'green': 0, 'blue': 0}

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
        for round in game:
            for color, color_max in colors.items():
                if round[color] > color_max: colors[color] = round[color]
        cube_minimums = tuple(colors.values())
        small_out = cube_minimums[0]
        for cube_minimum in cube_minimums[1:]:
            small_out *= cube_minimum
        sucess += small_out
        colors = {'red': 0, 'green': 0, 'blue': 0}
    print(sucess)

# I'm not even gonna try to make this a oneliner lol