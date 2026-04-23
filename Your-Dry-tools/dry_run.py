nums = [0,1,2,3,4]
index = [0,1,2,2,1]
res = []
for i in range(len(nums)):
    res.insert(index[i],nums[i])
print(res)