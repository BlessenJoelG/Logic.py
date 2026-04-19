nums,res = [1,2,3,4,5,6,7,8,9,0],[]
for i in range(len(nums)):
    if i%10 == nums[i]:
        res.append(i)
if len(res)>0:
    return(min(res))
else:
    return(-1)