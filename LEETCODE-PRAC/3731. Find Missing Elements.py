class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = set(nums)
        nums_copy = {_ for _ in range(min(nums),max(nums)+1)}
        return sorted(list(nums_copy.difference(nums)))
