class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        invst = {_ for _ in nums if nums.count(_) == 2}
        return(list(invst))
        
