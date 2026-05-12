for _ in range(int(input())):
    n,m = map(int,input().split())
    words,c = [],0
    for _ in range(n):
        words.append(input())
    for x in words:
        if m>=len(x):
            m =  m-len(x)
            c += 1
        else:
            break
    print(c)