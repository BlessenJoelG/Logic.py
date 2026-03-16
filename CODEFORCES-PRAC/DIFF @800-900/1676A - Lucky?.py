t = int(input())
for _ in range(t):
    tkt = [int(x) for x in input()]
    if sum(tkt[0:3]) == sum(tkt[3:]):
        print("YES")
    else:
        print("NO")
