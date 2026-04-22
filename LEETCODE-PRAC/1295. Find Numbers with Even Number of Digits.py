class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for x in nums:
            if (len(str(x)))%2 == 0:
                even += 1
        return even