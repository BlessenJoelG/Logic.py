t = int(input())
for _ in range(t):
    h_m = list(map(int,input().split()))
    print(1440-(h_m[0]*60+h_m[1]))
