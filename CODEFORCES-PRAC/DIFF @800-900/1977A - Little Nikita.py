n = int(input())
for _ in range(n):
    n_m = list(map(int,input().split()))
    if n_m[0]%2 == 0 and n_m[1]%2 == 0 and n_m[0]>=n_m[1]:
        print("YES")
    elif n_m[0]%2 != 0 and n_m[1]%2 != 0 and n_m[0]>=n_m[1]:
        print("YES")
    else:
        print("NO")