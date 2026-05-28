class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n,x = str(n),str(x)
        if n.startswith(x) == False and n.count(x)>=1:
            return True
        else:
            return False