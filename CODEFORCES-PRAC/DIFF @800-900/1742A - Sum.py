t = int(input())
for _ in range(t):
    abc = list(map(int,input().split()))
    if (abc[0]+abc[1] == abc[2]) or  (abc[1]+abc[2] == abc[0]) or  (abc[0]+abc[2] == abc[1]):
        print("YES")
    else:
        print("NO")
