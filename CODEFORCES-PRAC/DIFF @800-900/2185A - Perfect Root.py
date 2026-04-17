for _ in range(int(input())):
    n = int(input())
    sqr = [x**2 for x in range(1,n+1)]
    print(*sqr)