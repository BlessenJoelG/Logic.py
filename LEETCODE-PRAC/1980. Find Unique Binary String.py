class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(2**len(nums)):
            if format(i,f"0{len(nums)}b") not in nums:
                return format(i,f"0{len(nums)}b")