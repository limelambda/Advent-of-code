out = 0

with open('input') as schematic:
    num_dict = {}
    schem_lines = dict(enumerate(schematic.readlines()))  # I didn't wanna make this a dictionary but I couldn't think of a another way :/
    for line_num, line in schem_lines.items():
        num_list = [(index, value) for index, value in enumerate(line) if value.isdigit()]
        num_range = iter(range(len(num_list)))
        for num in num_range:
            length = 0
            while num + length < len(num_list) and num_list[num][0] + length == num_list[num + length][0]:
                length += 1
            length -= 1
            num_dict[(line_num, range(num_list[num][0], num_list[num + length][0] + 1))] = ''.join(num_tuple[1] for num_tuple in num_list[num:num+length+1])
            [next(num_range) for i in range(length)]
    sym_locations = []
    for line_num, line in schem_lines.items():
        [sym_locations.append((line_num, index)) for index, value in enumerate(line) if not (value.isdigit() or value == '.' or value == '\n')]
    # Finally done parsing the input lol
    for sym in sym_locations:
        for y in range(-1, 2):
            for x in range(-1, 2):
                try:
                    for num_location in list(num_dict.keys()):
                        if num_location[0] == sym[0] + y and sym[1] + x in num_location[1]:
                            out += int(num_dict[num_location])  # Seven layers of indentation, I'm so sorry
                            del num_dict[num_location]
                except IndexError:
                    continue

print(out)