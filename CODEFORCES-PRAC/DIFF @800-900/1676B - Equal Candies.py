t = int(input())
for _ in range(t):
    lst = sorted(list(map(int,input().split())))
    if len(set(lst)) == 1:
        print(0)
    else:
        for _ in range(1,len(lst)):
            lst[_] = lst[_] - lst[0]
        print(sum(lst[1:len(lst)]))