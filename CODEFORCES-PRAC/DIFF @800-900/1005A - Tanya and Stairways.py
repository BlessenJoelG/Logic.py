n = int(input())
stairs,res = list(map(int,input().split())),[]
for i in range(len(stairs)):
    if i == (len(stairs)-1):
        res.append(stairs[i])
    elif stairs[i]<stairs[i+1]:
        pass
    elif stairs[i]>=stairs[i+1]:
        res.append(stairs[i])
print(len(res))
print(*res)