class Solution:
    def maxProduct(self, n: int) -> int:
        digsplit,mul = sorted([int(x) for x in str(n)]),0
        return digsplit[-1]*digsplit[-2]
        