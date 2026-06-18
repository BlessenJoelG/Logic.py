groupSizes = [3,3,3,3,3,1,3]
grp = {}
for i in range(len(groupSizes)):
    if groupSizes[i] not in grp:
        grp[groupSizes[i]] = [i]
    else:
        grp[groupSizes[i]].append(i)
ans = []
for size,people in grp.items():
    for i in range(0,len(people),size):
        ans.append(people[i:i+size])
print(ans)