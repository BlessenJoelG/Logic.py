class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n,e,o = bin(n)[2:],0,0
        n = [int(x) for x in reversed(str(n))]
        for i in range(len(n)):
            if n[i] == 1 and i%2 == 0:
                e += 1
            elif n[i] == 1 and i%2 != 0:
                o += 1
        return([e,o])