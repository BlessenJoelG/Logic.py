class Solution:
    def countAsterisks(self, s: str) -> int:
        s,c = s.split("|"),0
        for i in range(0,len(s),2):
            c += s[i].count("*")
        return c