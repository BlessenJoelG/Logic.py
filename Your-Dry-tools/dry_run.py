n = format(n,"03b")
r,c = n[::-1],0
for i in range(len(n)):
    if n[i] != r[i]:
        c += 1
print(c)