nums = [96,89]
mini = float("inf")
for n in nums:
    curr = 0
    while(n>0):
        d = n%10
        curr += d
        n = n//10
    mini = min(mini,curr)
print(mini)