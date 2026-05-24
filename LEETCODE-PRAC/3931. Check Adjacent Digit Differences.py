class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        c =0
        for i in range(1,len(s)):
            if abs(int(s[i-1])-int(s[i])) <= 2:
                c += 1
        if c == len(s)-1:
            return True
        else:
            return False
