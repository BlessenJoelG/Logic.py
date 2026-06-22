rings = "B0R0G0R9R0B0G0"
freq,c = {},0
for i in range(0,len(rings),2):
    if rings[i+1] not in freq:
        freq[rings[i+1]] = [rings[i]]
    else:
        freq[rings[i+1]] += [rings[i]]
for x in freq.values():
    if len(set(x)) == 3:
        c += 1
print(c)