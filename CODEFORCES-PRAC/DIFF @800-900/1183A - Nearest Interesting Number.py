a = int(input())
while(a>0):
    if sum([int(x) for x in str(a)])%4 == 0:
        print(a)
        break
    a += 1