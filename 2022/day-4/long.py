data = open("input.txt", "rt").read().split('\n')[:-1]

data = [[[int(z) for z in y.split('-')] for y in x.split(',')] for x in data]

print(data)

for i in data:
    if (i[0][0] in range(i[1][0], i[1][1]+1) and i[0][1] in range(i[1][0], i[1][1]+1)) or (i[1][0] in range(i[0][0], i[0][1]+1) and i[1][1] in range(i[0][0], i[0][1]+1)):
        print('yo!')
        #from here I worked on main.py

#... for pt2 just change the ands to or-s