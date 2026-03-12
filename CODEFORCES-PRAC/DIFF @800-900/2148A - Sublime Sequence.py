t = int(input())
for _ in range(t):
    x_n = list(map(int,input().split()))
    if x_n[1]%2 == 0:
        print(0)
    else:
        print(x_n[0])
