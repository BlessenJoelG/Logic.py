class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x = str(x)
        x_div = sum([int(_) for _ in x])
        if int(x)%x_div == 0:
            return(x_div)
        else:
            return(-1)
