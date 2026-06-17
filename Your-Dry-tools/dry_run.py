n = 122
n = [int(x) for x in str(n)]
ans = 0
for x in set(n):
    ans = ans + x*n.count(x)
print(ans)