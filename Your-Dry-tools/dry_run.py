s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
freq,ans = {},""
if indices == sorted(indices):
    print(s)
else:
    for i in range(len(indices)):
        freq[indices[i]] = s[i]
    for x in sorted(freq.keys()):
        ans += freq[x]
    print(ans)