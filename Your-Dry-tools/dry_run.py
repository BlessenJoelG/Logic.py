nums,k,sum = [4,3,2,1],2,0
for i in range(len(nums)):
    n = (format(i,"b"))
    if n.count("1") == k:
        sum += nums[i]
print(sum)