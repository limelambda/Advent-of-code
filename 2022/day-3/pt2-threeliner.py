new_data = [[]]
[new_data[-1].append(i) if len(new_data[-1]) != 3 else new_data.append([i]) for i in open("input", "rt").read().split('\n')]
print(sum([{'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52,}[i] for i in [[y for y in set(x[0]) if y in set(x[1]) and y in set(x[2])][0] for x in new_data]]))

# Idk I'm going back through these and making them consistent and doing a few quick fixes and I'm sure this can actaully be a one liner but then it would be a quick fix now would it?