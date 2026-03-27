t = int(input())
for _ in range(t):
    res = input()
    res = res.lower()
    res = [res[_] for _ in range(len(res)) ]
    if ["y","e","s"] == res:
        print("YES")
    else:
        print("NO")
    res.clear()
