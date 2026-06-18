key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
key = "".join(key.split(" "))
ans = []
for x in key:
    if x not in ans:
        ans.append(x)
key = "".join(ans)
freq = {}
i,j = 97,0
while(i<=122):
    if key[j] not in freq:
        freq[key[j]] = chr(i)
    i += 1
    j += 1
res = ""
for x in message:
    if x == " ":
        res = res + " "
    else:
        res = res + freq[x]
print(res)