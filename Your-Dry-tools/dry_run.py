freq,val = {},True
for x in s:
    if x not in freq:
        freq[x] = 1
    else:
        freq[x] += 1
for x in freq:
    if freq.get(x) != max(freq.values()):
        val = False
        break
print(val)