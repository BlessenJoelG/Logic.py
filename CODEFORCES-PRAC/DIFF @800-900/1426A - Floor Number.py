import math as m
for _ in range(int(input())):
    n,x = map(int,input().split())
    if n == 1 or n == 2:
        print(1)
    else:
        print(m.ceil((n-2)/x)+1)