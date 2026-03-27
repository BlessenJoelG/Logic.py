t = int(input())
lst = ["A","B","C"]
for _ in range(t):
    for _ in range(3):
        chk = [x for x in input()]
        for x in lst:
            if x not in chk:
                print(x)
                break