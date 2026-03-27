t = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
for _ in range(t):
    n = int(input())
    s = [_ for _ in input()]
    s.sort()
    print(alpha.index(s[len(s)-1])+1)
