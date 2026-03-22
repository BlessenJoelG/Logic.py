class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1,c2 = 0,0
        for x in nums1:
            if x in nums2:
                c1 = c1 + 1
        for y in nums2:
            if y in nums1:
                c2 = c2 + 1
        return([c1,c2])
