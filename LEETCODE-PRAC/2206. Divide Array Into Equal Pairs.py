class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq,n,c = {},len(nums)//2,0
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        for x in freq.values():
            c += x//2
        return c == n