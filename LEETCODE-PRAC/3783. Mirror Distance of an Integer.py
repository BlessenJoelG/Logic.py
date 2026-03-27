class Solution:
    def mirrorDistance(self, n: int) -> int:
        revs = int(str(n)[::-1])
        return(abs(n-revs))
