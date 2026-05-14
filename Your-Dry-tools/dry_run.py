arr = [400]
nums = []
for i in range(0,len(arr)-1):
    nums.append(max(arr[i+1:]))
nums.append(-1)
print(nums)