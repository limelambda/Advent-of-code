print('{', end = '')
for i in range(52):
    print(f"'{'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[i]}':{i+1},", end = '')
print('}')
print('\nThat was how I got the dict I\'m not doing that manually so I just had it print to the console\n')


def calc_sum_from_duplicates(duplicates):
    return sum([{
        'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
        'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52,
        }[i] for i in duplicates])

data = open("input", "rt").read().split('\n')

duplicates = [[y for y in set(x[:int(len(x) / 2)]) if y in set(x[int(len(x) / 2):])][0] for x in data]
print(calc_sum_from_duplicates(duplicates))