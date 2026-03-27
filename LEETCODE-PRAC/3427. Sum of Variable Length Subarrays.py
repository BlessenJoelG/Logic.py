class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0 
        for i in range(len(nums)):
            strt = max(0,i-nums[i])
            total = total + sum(nums[strt:i+1])
        return total
