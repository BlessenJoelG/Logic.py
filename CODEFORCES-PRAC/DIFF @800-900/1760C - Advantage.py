for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    nums_srt = sorted(nums)
    res = []
    for i in range(len(nums)):
        if nums[i] == nums_srt[len(nums_srt)-1]:
            res.append(nums[i]-nums_srt[len(nums_srt)-2])
        else:
            res.append(nums[i]-nums_srt[len(nums_srt)-1])
    print(*res)