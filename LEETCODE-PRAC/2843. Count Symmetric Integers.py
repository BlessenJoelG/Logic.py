class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for x in range(low,high+1):
            x = [int(i) for i in str(x)]
            if len(x)==1 or len(x)%2!=0:
                pass
            else:
                if sum(x[:(len(x)//2)]) == sum(x[(len(x)//2):]):
                    c += 1
        return(c)
