class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums_digi = []
        def num_split(a):
            for _ in str(a):
                nums_digi.append(int(_))
            return nums_digi
        for _ in nums:
            num_split(_)
        return(nums_digi)
