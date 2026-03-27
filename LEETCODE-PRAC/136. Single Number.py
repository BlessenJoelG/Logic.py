class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = [x for x in nums if nums.count(x)==1]
        return(nums[0])
