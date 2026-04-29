class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        return sum(int(n[i]) if i & 1 == 0 else -1*int(n[i]) for i in range(len(n)))
