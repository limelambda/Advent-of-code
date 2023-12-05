def main():
    def run_conversions(seed):
        for conversion_map in maps:
            for which_range in range(len(conversion_map)):
                if seed in range(conversion_map[which_range][1], conversion_map[which_range][1] + conversion_map[which_range][2]):
                    seed = seed - conversion_map[which_range][1] + conversion_map[which_range][0]
                    break
        return seed

    with open('input') as almanac:
        almanac = almanac.read()
    seeds = [int(i) for i in almanac.split('\n')[0].split(' ')[1:]]
    maps = [[[int(n) for n in j.split(' ')] for j in i.split('\n')[1:]] for i in almanac.split('\n\n')[1:]]
    values = list(map(run_conversions, seeds))
    print(min(values), values)

main()