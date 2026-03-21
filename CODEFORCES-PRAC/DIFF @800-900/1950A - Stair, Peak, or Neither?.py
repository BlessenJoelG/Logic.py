t = int(input())
for z in range(t):
    abc = list(map(int,input().split()))
    if abc[0]<abc[1]<abc[2]:
        print("STAIR")
    elif abc[0]<abc[1]>abc[2]:
        print("PEAK")
    else:
        print("NONE")
