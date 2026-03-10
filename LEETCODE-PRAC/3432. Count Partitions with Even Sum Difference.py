class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        eve_cfm = 0
        for _ in range(0,len(nums)-1):
            eve_chk = (sum(nums[:_+1])-sum(nums[_+1:len(nums)]))
            if eve_chk%2 == 0:
                eve_cfm = eve_cfm + 1
        return(eve_cfm)
