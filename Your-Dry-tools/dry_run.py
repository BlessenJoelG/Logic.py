arr = [-3,0,1,-3,1,1,1,-3,10,0]
freq = {}
for x in arr:
    if x not in freq:
        freq[x] = 1
    else:
        freq[x] += 1
print(len(set(arr)) == len(set(freq.values())))