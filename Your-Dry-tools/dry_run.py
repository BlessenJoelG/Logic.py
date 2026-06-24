nums = [1,2,2,1]
freq,ans = {},[]
for x in nums:
    if x not in freq:
        freq[x] = 1
    else:
        freq[x] += 1
for x in freq.keys():
    if freq[x] == 2:
        ans.append(x)
if len(ans) == 0:
    print(0)
elif len(ans) == 1:
    print(1)
else:
    x = ans[0]
    for i in range(1,len(ans)):
        x ^= ans[i]
print(x)