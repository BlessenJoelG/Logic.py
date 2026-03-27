t = int(input())
for x in range(t):
    side_of_square = set(map(int,input().split()))
    if len(side_of_square) == 1:
        print("YES")
    else:
        print("NO")
