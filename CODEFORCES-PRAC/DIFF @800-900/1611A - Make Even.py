for _ in range(int(input())):
    n = str(int(input()))
    if int(n[len(n)-1])&1 == 0:
        print(0)
    elif int(n[0])&1 == 0:
        print(1)
    elif any(int(x)%2 ==0 for x in n ):
        print(2)
    else:
        print(-1)
