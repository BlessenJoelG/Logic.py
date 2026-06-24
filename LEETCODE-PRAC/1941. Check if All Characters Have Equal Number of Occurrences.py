class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for x in s:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        for x in freq:
            if freq.get(x) != max(freq.values()):
                return False
        return True