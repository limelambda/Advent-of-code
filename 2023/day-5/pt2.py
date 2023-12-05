def main():
    global val
    def run_conversions(seed):
        for conversion_map in maps:
            for which_range in range(len(conversion_map)):
                if seed in range(conversion_map[which_range][1], conversion_map[which_range][1] + conversion_map[which_range][2]):
                    seed = seed - conversion_map[which_range][1] + conversion_map[which_range][0]
                    break
        return seed

    with open('input') as almanac:
        almanac = almanac.read()
    file_seed_ranges = [int(i) for i in almanac.split('\n')[0].split(' ')[1:]]
    seed_ranges = [range(file_seed_ranges[::2][i],file_seed_ranges[::2][i] + file_seed_ranges[1::2][i]) for i in range(len(file_seed_ranges)//2)]
    maps = [[[int(n) for n in j.split(' ')] for j in i.split('\n')[1:]] for i in almanac.split('\n\n')[1:]]
    vals = []
    for seed_range_index, seed_range in enumerate(seed_ranges):
        print(f'Running seed range {seed_range_index} of {len(seed_ranges)}')
        vals.append(min(map(run_conversions, seed_range)))

    val = (min(vals))
    

main()

out = open('out.txt', 'w')
out.write(str(val) + '\n')
out.close()