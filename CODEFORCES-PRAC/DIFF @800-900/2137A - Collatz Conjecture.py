for i in range(int(input())):
    k,x = map(int,input().split())
    for _ in range(1,k+1):
        if (x-1)%3==0 and ((x-1)//3)%2==1:
            x = (x-1)//3
        else:
            x = x*2
    print(x)