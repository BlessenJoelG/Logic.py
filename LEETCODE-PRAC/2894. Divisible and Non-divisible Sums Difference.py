class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (sum([_ for _ in range(1,n+1) if _%m != 0]) - sum([_ for _ in range(1,n+1) if _%m == 0]))
