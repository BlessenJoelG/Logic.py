n_k = list(map(int,input().split()))
res = []
for _ in range(1,n_k[0],2):
        res.append(_)
for _ in range(2,n_k[0],2):
        res.append(_)
print(res)
print(res[n_k[1]-1])