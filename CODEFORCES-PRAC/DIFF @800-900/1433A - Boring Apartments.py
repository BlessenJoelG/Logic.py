for _ in range(int(input())):
    res,n,ans = [],str(int(input())),0
    for x in range(1,10):
        res.extend([str(x)*i for i in range(1,5)])
    for i in range(0,res.index(n)+1):
        ans += len(res[i])
    print(ans)