class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single,double = 0,0
        for x in nums:
            if x<10:
                single += x
            else:
                double += x
        if single>double or double>single:
            return(True)
        else:
            return(False)