n = int(input())
nums = list(map(int,input().split()))
top = max(nums)
c = 0
for x in nums:
    c = c + (top-x)
print(c)