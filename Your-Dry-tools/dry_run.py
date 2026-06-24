items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]
freq1,freq2,ans = {},{},[]
for x in items1:
    freq1[x[0]] = x[1]
for x in items2:
    freq2[x[0]] = x[1]
for x in freq1.keys():
    if x in freq2:
        ans.append([x,freq1[x]+freq2[x]])
    else:
        ans.append([x,freq1[x]])
for x in freq2.keys():
    if x not in freq1:
        ans.append([x,freq2[x]])
print(sorted(ans))