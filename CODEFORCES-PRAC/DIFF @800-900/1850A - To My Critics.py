for _ in range(int(input())):
    num = sorted(list(map(int,input().split())))
    if num[1]+num[2] >= 10:
        print("YES")
    else:
        print("NO")
