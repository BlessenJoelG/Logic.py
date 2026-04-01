nums = [3,1,2,10,1]
res = [sum(nums[:i+1]) for i in range(len(nums))]
print(res)