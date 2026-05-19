nums1 = [1,2,3]
nums2 = [7,2,4]
if set(nums1).intersection(set(nums2)):
    print(min(set(nums1).intersection(set(nums2))))
else:
    print(-1)