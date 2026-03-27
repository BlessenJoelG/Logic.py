class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        c = 0
        nums_eve =[_ for _ in nums if _%2==0]
        for x in nums_eve:
            c = c|x
        return(c) 
