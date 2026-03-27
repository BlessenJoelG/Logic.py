class Solution:
    def minElement(self, nums: List[int]) -> int:
        nums_split = [str(_) for _ in nums]
        i = 0
        while(i!=len(nums)):
            for x in nums_split:
                dig_sum = 0
                for _ in range(len(x)):
                    dig_sum = dig_sum + int(x[_])
                nums[i] = int(dig_sum)
                i = i + 1
        return(min(nums))    
