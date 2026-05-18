encoded = [1,2,3]
first = 1
ans = []
ans.append(first)
for _ in range(len(encoded)):
    ans.append(ans[_]^encoded[_])
print(ans)