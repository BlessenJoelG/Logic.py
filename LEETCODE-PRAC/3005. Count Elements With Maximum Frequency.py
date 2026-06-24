class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq,c = {},0
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        for x in freq:
            if freq.get(x) == max(freq.values()):
                c += freq.get(x)
        return c