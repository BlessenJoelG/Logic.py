for _ in range(int(input())):
    a,b,k = map(int,input().split())
    if k&1 == 1:
        print(a*(k//2)-b*(k//2)+a)
    else:
        print(a*(k//2)-b*(k//2))