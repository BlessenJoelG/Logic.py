s = "Myself2 Me1 I4 and3"
freq,c = {},""
for x in list(s.split(" ")):
    if x not in freq:
        freq[x[-1]] = x[:]
for x in sorted(freq.keys()):
    c += freq[x]
for i in range(len(c)):
    if c[i].isalpha() == False:
        c = c.replace(c[i]," ")
print(c)