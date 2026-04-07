txt = input()
u,o = 0,0
for _ in txt:
    if _.isupper():
        u += 1
    else:
        o += 1
if u > o:
    print(txt.upper())
else:
    print(txt.lower())