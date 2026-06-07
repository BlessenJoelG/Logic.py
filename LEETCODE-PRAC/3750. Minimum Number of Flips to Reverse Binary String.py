class Solution:
    def minimumFlips(self, n: int) -> int:
        n = format(n,"b")
        r,c = n[::-1],0
        for i in range(len(n)):
            if n[i] != r[i]:
                c += 1
        return c