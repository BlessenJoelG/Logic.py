class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def calcGCD(a,b):
            while b:
                a,b = b,a%b
            return a
        sumOdd = sum([_ for _ in range(2*n) if _%2 != 0])
        sumEve = sum([_ for _ in range(2*n+1) if _%2 == 0])
        return(calcGCD(sumEve,sumOdd))
