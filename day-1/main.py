print(max([sum([int(y) for y in x.split('\n')]) for x in open("input.txt", "rt").read().split('\n\n')[:-1]]))
print('pt1 ^ pt2 v')
out = ([sum([int(y) for y in x.split('\n')]) for x in open("input.txt", "rt").read().split('\n\n')[:-1]]);out.sort();print(sum((out)[-3:]))