arr = ["aaa","aa","a"]
k = 1
ans = []
for x in arr:
    if arr.count(x) == 1:
        ans.append(x)
print(ans)
if len(ans)<=k-1:
    print('""')
else:
    print(ans[k-1])