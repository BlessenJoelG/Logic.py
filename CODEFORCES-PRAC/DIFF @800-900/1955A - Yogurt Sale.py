for i in range(int(input())):
    n,a,b = map(int,input().split())
    nums,c = [],0
    if n%2 == 0:
        for _ in range((n//2)):
            nums.append(2)
    else:
        for _ in range((n-1)//2):
            nums.append(2)
        nums.append(1)
    for x in nums:
        if x == 1:
            c += a
        elif x == 2:
            if 2*a < b:
                c += 2*a
            else:
                c += b
    print(c)