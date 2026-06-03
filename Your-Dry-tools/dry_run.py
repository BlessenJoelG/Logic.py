class Solution:
    def largeEven(self,x,i):
        while(i!=0):
            if int(x)%2==0:
                return x
            else:
                i = i-1
                x = x[0:i]
        return x
s = input()
i = len(str(s))
ans = Solution()
print(ans.largeEven(s,i))