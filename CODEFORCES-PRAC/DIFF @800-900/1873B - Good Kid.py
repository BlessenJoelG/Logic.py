t = int(input())
for _ in range(t):
    dig_len,mul = int(input()),1
    dig = list(map(int,input().split()))
    dig[dig.index((min(dig)))] = dig[dig.index((min(dig)))] + 1
    for x in dig:
        mul = mul * x
    dig.clear()
    print(mul)
