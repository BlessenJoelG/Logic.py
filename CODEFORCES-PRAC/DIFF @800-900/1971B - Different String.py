t = int(input())
for _ in range(t):
    name = input()
    if len(set(name)) == 1:
        print("NO")
    else:
        print("YES")
        rev = name[::-1]
        if rev == name:
            print(name[1:] + name[0])
        else:
            print(rev)
