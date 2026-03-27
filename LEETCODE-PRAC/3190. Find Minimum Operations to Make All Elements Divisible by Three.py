class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        for _ in nums:
            if _%3!=0:
                c = c+1
        return(c) 