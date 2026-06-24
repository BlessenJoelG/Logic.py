class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        return len(set(arr)) == len(set(freq.values()))