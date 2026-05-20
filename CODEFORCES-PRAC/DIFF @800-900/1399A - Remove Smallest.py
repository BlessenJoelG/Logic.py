for _ in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int,input().split())))
    i = 0
    while(len(nums)!=1):
        if abs(nums[i]-nums[i+1]) <= 1:
            nums.remove(min(nums[i],nums[i+1]))
        else:
            break
    if len(nums) == 1:
        print("YES")
    else:
        print("NO")