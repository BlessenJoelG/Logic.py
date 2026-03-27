class Solution:
    def evenlyDivides(self, n):
        c = 0
        dig_split = [int(_) for _ in str(n)]
        for x in dig_split:
            if x == 0:
                pass
            elif n%x == 0:
                c = c + 1
        return c