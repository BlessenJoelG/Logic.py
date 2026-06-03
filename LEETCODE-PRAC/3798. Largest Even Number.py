class Solution:
    def largestEven(self, s: str) -> str:
        i = len(s)
        while(i!=0):
            if int(s)%2==0:
                return s
            else:
                i = i-1
                s = s[0:i]
        return s