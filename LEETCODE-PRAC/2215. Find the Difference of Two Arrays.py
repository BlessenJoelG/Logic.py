class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1,ans2 = [],[]
        for x in nums1:
            if x not in nums2:
                ans1.append(x)
        for x in nums2:
            if x not in nums1:
                ans2.append(x)
        return [list(set(ans1)),list(set(ans2))]