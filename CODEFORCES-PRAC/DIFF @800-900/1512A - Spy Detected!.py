t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    for _ in arr:
        if arr.count(_) == 1:
            print(arr.index(_)+1)
