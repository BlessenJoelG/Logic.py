nums = [10,4,8,3]
ls,rs,res =[],[],[]
for i in range(len(nums)):
    ls.append(sum(nums[:i]))
nums = nums[::-1]
for i in range(len(nums)):
    rs.append(sum(nums[:i]))
rs = rs[::-1]
for i in range(len(nums)):
    res.append(abs(ls[i]-rs[i]))
print(res)