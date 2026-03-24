t = int(input())
ans = ["T","i","m","r","u"]
for _ in range(t):
    length = int(input())
    s = [x for x in input()]
    s.sort()
    if ans == s:
        print("YES")
    else:
        print("NO")
