n,e,o = bin(int(input()))[2:],0,0
n = [int(x) for x in reversed(str(n))]
for i in range(len(n)):
    if n[i] == 1 and i%2 == 0:
        e += 1
    elif n[i] == 1 and i%2 != 0:
        o += 1
print([e,o])