for _ in range(int(input())):
    s = input()
    x = sorted([ord(i) for i in s])
    val = True
    for i in range(len(x)-1):
        if abs(x[i]-x[i+1]) != 1:
            val = False
            break
    if val == True:
        print("YES")
    else:
        print("NO")