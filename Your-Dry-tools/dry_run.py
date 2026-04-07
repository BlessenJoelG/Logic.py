title = "First leTTeR of EACH Word"
title = title.split(" ")
res = []
for x in title:
    if len(x)>3:
        res.append(x[0].upper()+x[1:].lower())
    else:
        res.append(x.lower())
print(" ".join(res))