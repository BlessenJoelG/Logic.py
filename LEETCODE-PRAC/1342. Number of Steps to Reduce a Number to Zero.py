class Solution:
    def numberOfSteps(self, num: int) -> int:
        n,steps = num,0
        while(n != 0):
            if n%2 == 0:
                n = int(n/2)
                steps = steps + 1
            else:
                n = n - 1
                steps = steps + 1
        return(steps)      