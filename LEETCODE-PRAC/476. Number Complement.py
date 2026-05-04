class Solution:
    def findComplement(self, num: int) -> int:
        n = (format(num,"b"))
        n = n.replace("0","z")
        n = n.replace("1","o")
        n = n.replace("z","1")
        n = n.replace("o","0")
        return(int(n,2))
