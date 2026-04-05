t = int(input())
for _ in range(t):
    nums = sorted(list(map(int,input().split())))
    print((sum((nums)[0:6])*-1)+nums[6])