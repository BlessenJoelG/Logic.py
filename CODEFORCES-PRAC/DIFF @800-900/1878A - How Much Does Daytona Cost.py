for _ in range(int(input())):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    if k in nums:
        print("YES")
    else:
        print("NO")