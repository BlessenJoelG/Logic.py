class Solution:
    def addDigits(self, num: int) -> int:
        def digit_sum(a):
            dig_sum = 0
            x = str(a)
            for y in x:
                dig_sum = dig_sum + int(y)
            return(dig_sum)
        while(len(str(num))!=1):
            num = digit_sum(num)
        return(num)
