for _ in range(int(input())):
    n = int(input())
    num,res = list(map(int,input().split())),[]
    i,j = 0,n-1
    while(i<=j):
        res.append(num[i])
        if i==j:
            break
        i += 1
        res.append(num[j])
        j -= 1
    print(*res)
