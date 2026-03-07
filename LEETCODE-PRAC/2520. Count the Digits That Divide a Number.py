class Solution:
    def countDigits(self, num: int) -> int:
        num_str,dig_div = str(num),0
        dig_of_num = [int(num_str[_]) for _ in range(len(num_str))]
        for x in dig_of_num:
            if num%x == 0:
                dig_div = dig_div + 1
        return(dig_div)