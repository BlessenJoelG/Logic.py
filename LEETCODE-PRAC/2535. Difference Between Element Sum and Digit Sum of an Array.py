class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        dig_sum = 0
        for x in nums:
            x = str(x)
            for y in x:
                dig_sum = dig_sum + int(y)
        return(abs(sum(nums)-dig_sum))
