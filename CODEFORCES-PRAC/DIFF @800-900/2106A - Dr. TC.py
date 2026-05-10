for y in range(int(input())):
    n = int(input())
    s,res = input(),[]
    for _ in range(len(s)):
        x = [int(i) for i in s]
        if s[_] == "1":
            x[_] = 0
        else:
            x[_] = 1
        res.extend(x)
    print(res.count(1))