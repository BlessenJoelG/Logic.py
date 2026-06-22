nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
freq,res = {},[]
for x in nums1:
    if x[0] not in freq:
        freq[x[0]] = x[1]
for x in nums2:
    if x[0] not in freq:
        freq[x[0]] = x[1]
    else:
        freq[x[0]] += x[1]
for x in freq.items():
    res.append(list(x))
print(sorted(res))