class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = str(nums)[1:-1]
        s = s[::-1]
        l = s.split(" ,")
        l = list(map(int, l ))
        nums += l
        return (len(set(nums)))