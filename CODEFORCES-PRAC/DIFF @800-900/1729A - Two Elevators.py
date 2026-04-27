for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if abs(a-1)<abs(b-c)+abs(c-1):
        print(1)
    elif abs(b-c)+abs(c-1)<abs(a-1):
        print(2)
    else:
        print(3)