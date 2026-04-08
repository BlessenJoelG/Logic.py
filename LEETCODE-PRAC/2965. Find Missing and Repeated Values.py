class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        miss_val = [x for x in range(1,(len(grid)**2)+1)]
        repeat = []
        ans = []
        for x in grid:
            repeat.extend(x)
        for y in repeat:
            if repeat.count(y)>1:
                ans.append(y)
                break
        for z in miss_val:
            if z not in repeat:
                ans.append(z)
                break
        return ans