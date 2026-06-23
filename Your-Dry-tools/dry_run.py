nums = ["01","10"]
ans = []
for i in range(2**len(nums)):
    if format(i,f"0{len(nums)}b") not in nums:
        print(format(i,f"0{len(nums)}b"))
        break