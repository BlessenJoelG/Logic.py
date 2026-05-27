events = ["W","W","W","W","W","W","W","W","W","W","W"]
s,c = 0,0
for i in events:
    if c == 10:
        break
    else:
        if i == "W":
            c += 1
        elif i == "WD" or i == "NB":
            s += 1
        else:
            s += int(i)
print([s,c])