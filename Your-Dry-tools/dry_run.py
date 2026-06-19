gain = [-5,1,5,0,-7]
ans = [0]
for i in range(len(gain)):
    ans.append(gain[i]+ans[i])
print(max(ans))