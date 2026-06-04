class Solution:
    def isFascinating(self, n: int) -> bool:
        n = sorted([x for x in (str(n)+str(2*n)+str(3*n))])
        if ['1','2','3','4','5','6','7','8','9'] == n:
            return True
        else:
            return False