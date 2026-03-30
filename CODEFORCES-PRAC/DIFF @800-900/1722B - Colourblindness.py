t= int(input())
for _ in range(t):
    n = int(input())
    str1 = input()
    str2 = input()
    c = 0
    for i in range(n):
        if ((str1[i]=="G" and str2[i]=="B") or (str1[i]=="B" and str2[i]=="G")):
            c += 1
        elif str1[i] == str2[i]:
            c += 1
        else:
            break
    if c == n:
        print("YES")
    else:
        print("NO")