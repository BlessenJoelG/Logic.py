import math
for _ in range(int(input())):
    n = int(input())
    nums = sum(map(int,input().split()))
    print(math.ceil(nums/n))