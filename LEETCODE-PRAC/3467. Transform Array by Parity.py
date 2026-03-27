class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        nums = sorted([0 if _%2 == 0 else 1 for _ in nums])
        return(nums)
