print(sum([{'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9,'C X':7, 'C Y':2, 'C Z':6}[i] for i in open("input.txt", "rt").read().split('\n')[:-1]]))
print('pt1 ^ pt2 v')
print(sum([{'A Y':4, 'A Z':8, 'A X':3,'B X':1, 'B Y':5, 'B Z':9,'C Z':7, 'C X':2, 'C Y':6}[i] for i in open("input.txt", "rt").read().split('\n')[:-1]]))