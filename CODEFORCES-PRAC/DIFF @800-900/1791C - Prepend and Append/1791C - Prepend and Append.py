for _ in range(int(input())):
    n = int(input())
    s = input()
    i,j = 0,n-1
    while(s[i]!=s[j]):
        if i>j and s[i] != s[j]:
            break
        i += 1
        j -= 1
    print(len(s[i:j+1]))
