t = int(input())
for x in range(t):
    alpha = input()
    if alpha == "abc" or alpha == "acb" or alpha == "bac" or alpha == "cba":
        print("YES")
    else:
        print("NO")
