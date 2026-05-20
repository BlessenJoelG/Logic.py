class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        c,i = 0,0
        while(nums[i] < k):
            nums.remove(nums[i])
            c += 1
        return(c)