class Solution:
    def removeZeros(self, n: int) -> int:
        s = ""
        for x in str(n):
            if int(x) > 0:
                s += x
        return (int(s))