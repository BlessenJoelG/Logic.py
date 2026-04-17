for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    max_idx = nums.index(max(nums))
    if nums[0] != max(nums):
        temp = nums[0]
        nums[0] = max(nums)
        nums[max_idx] = temp
    c = 0
    for k in range(1,n+1):
        digi = nums[0:k]
        c += max(digi)
    print(c)