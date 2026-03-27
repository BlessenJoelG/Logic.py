t = int(input())
for _ in range(t):
    count = 0 
    players = list(map(int,input().split()))
    for i in range(1,4):
        if players[0] < players[i]:
            count = count + 1
    print(count)
