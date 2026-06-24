class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
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
        return list(ans)
    
"""ANOTHER TRICK OF DOING THIS Q USING BITWISE:
s1,s2,s3=set(nums1),set(nums2),set(nums3)
return list((s1&s2) | (s2&s3) | (s3&s1))"""
