t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    nums = list(map(int,input().split()))
    for i in range(n):
        if i%2==0:
            res.append(nums[i])
        else:
            res.append(nums[i]*-1)
print(sum(res))