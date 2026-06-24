nums = [5,1,5,2,5,3,5,4]
for x in nums:
    if nums.count(x) == (len(nums)//2):
        print(x)
        break