s = "z*#"
res = ""
for x in s:
    if x.isalpha():
        res = res + x
    elif x == "*" and len(res)>=1:
        res = res[:-1]
    elif x == "#":
        res = res+res
    elif x == "%":
        res = res[::-1]
print(res)