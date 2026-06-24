class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for x in nums:
            if nums.count(x) == (len(nums)//2):
                return x