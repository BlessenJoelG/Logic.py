class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)//2):
            freq = nums[2*i]
            val = nums[2*i+1]
            res.extend([val]*freq)
        return res
