words = ["abcd"]
weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
w,f = {},{}
i,j = 97,0
while(i<=122):
    w[chr(i)] = weights[j]
    i += 1
    j += 1
i,j = 122,0
while(i>=97):
    f[j] = chr(i)
    i -= 1
    j += 1
ans = ""
for word in words:
    ans = ans + f.get((sum(w[x] for x in word))%26)
print(ans)  