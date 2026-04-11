class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        numzz = []
        for x in nums:
            if x%2 == 0:
                numzz.append(x)
        for x in nums:
            if x%2 != 0:
                numzz.append(x)
        return numzz