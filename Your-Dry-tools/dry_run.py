nums = [-1,5,7,0]
a,b = [],[]
bool = False
for i in range(len(nums)):
    if i>1:
        bool = True
        for j in range(2,i):
            if i%j == 0:
                bool = False
                break
    if bool:
        a.append(nums[i])
    else:
        b.append(nums[i])
print(abs(sum(a)-sum(b)))