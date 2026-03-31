class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if j == i:
                    continue
                elif nums[i]>nums[j]:
                    c = c+1
            result.append(c)
        return(result)