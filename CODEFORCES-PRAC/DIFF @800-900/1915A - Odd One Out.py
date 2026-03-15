t = int(input())
for _ in range(t):
    nums = list(map(int,input().split()))
    for _ in nums:
        if nums.count(_)==1:
            print(_)