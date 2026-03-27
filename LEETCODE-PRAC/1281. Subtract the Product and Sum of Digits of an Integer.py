class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        n = [int(n[_]) for _ in range(len(n))]
        dig_total,dig_multi = sum(n),prod(n)
        return(dig_multi - dig_total)
