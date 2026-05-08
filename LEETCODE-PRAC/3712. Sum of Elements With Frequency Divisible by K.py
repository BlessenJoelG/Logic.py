class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        res = 0
        for x in nums:
            if nums.count(x)%k == 0:
                res += x
        return res
