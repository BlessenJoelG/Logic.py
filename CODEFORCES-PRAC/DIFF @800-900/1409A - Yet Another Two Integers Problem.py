import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    low,high = min(a,b),max(a,b)
    print(math.ceil((high-low)/10))