for _ in range(int(input())):
    a,b,n,s = map(int,input().split())
    use = min(a, s//n)  
    rem = s - use*n
    if rem <= b:
        print("YES")
    else:
        print("NO")
