class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(len(nums)):
            ans.append(nums[nums[_]])
        return ans