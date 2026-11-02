class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        a,b = format(a,"b"),format(b,"b")
        s1,s2 = a.count("1"),b.count("1")
        if s1>=s2:
            return s1*s2
        else:
            return int(s2/s1)
