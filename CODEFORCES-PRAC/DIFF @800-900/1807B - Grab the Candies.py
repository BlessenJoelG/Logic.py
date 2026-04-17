for _ in range(int(input())):
    n = int(input())
    eve,odd = 0,0
    cand = list(map(int,input().split()))
    for x in cand:
        if x%2 == 0:
            eve = eve + x
        else:
            odd = odd + x
    if eve > odd:
        print("YES")
    else:
        print("NO")