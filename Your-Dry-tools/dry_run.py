for _ in range(int(input())):
    n,m = map(int,input().split())
    x,s,c = input(),input(),0
    if len(x)>len(s):
        c = -1
    while(len(x)<=len(s)):
        x = x+x
        c += 1
    print(c)