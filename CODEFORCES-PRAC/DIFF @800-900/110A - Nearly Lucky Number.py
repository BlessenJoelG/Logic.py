nums = int(input())
nums = [int(x) for x in str(nums)]
if nums.count(4) + nums.count(7) == 4 or nums.count(4) + nums.count(7) == 7:
    print("YES")
else:
    print("NO")