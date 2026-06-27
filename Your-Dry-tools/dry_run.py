nums = [1,2,3,4,5]
ans = []
for i in range(len(nums)):
    ans.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
print(ans)