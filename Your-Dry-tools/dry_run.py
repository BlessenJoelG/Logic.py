a_nums = list(map(int,input().split()))
b_nums = list(map(int,input().split()))
res = []
for x in a_nums:
    res.append(b_nums[0]-x)
print(res)
if res == sorted(res):
    print("YES")
else:
    print("NO")