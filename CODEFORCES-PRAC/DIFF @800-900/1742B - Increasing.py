t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    if n == len(set(lst)):
        print("YES")
    else:
        print("NO")