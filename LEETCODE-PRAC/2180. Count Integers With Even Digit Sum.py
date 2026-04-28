class Solution:
    def countEven(self, num: int) -> int:
       c = 0
       for a in range(1,num+1):
            if sum([int(x) for x in str(a)])%2 == 0:
                c += 1
       return(c) 