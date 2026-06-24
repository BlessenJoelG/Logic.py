nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
ans = set()
for x in set(nums1):
    if x in nums2:
        ans.add(x)
for x in set(nums2):
    if x in nums3:
        ans.add(x)
for x in set(nums3):
    if x in nums1:
        ans.add(x)
print(list(ans))