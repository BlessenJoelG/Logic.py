class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_sqr = [_*_ for _ in nums]
        nums_sqr.sort()
        return(nums_sqr)
