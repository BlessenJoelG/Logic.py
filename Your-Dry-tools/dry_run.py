nums = [3,2,3,2,2,2]
freq,n,c = {},len(nums)//2,0
for x in nums:
    if x not in freq:
        freq[x] = 1
    else:
        freq[x] += 1
for x in freq.values():
    c += x//2
print(c == n)