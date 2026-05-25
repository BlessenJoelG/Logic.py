for _ in range(int(input())):
    n,c = int(input()),0
    while(n!=1):
        if n%2 == 0:
            n = n//2
            c += 1
        elif n%3 == 0:
            n = (2*n)//3
            c += 1
        elif n%5 == 0:
            n = (4*n)//5
            c += 1
        elif n%2 != 0 and n%3 != 0 and n%5 != 0:
            c = -1
            break
    print(c)
