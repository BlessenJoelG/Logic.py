class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (sum(x for x in range(0,len(nums)+1))-sum(nums))