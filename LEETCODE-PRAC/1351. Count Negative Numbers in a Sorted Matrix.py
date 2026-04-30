class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for lst in grid:
            for x in lst:
                if x<0:
                    c += 1
        return(c)