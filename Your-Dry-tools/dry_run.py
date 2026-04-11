numzz = []
for x in nums:
    if x%2 == 0:
        numzz.append(x)
for x in nums:
    if x%2 != 0:
        numzz.append(x)
return numzz