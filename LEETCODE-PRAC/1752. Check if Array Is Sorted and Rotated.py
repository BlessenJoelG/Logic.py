class Solution:
    def check(self, nums: List[int]) -> bool:
        ans = sorted(nums)
        bool = False
        for i in range(len(nums),-1,-1):
            if ans == (nums[i:]+nums[:i]):
                bool = True
                break
        return bool