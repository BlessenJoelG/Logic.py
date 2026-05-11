for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    c = 0
    for x in set(nums):
            c += nums.count(x)//2
    print(c)