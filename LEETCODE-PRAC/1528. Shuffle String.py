class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        freq,ans = {},""
        if indices == sorted(indices):
            return s
        else:
            for i in range(len(indices)):
                freq[indices[i]] = s[i]
            for x in sorted(freq.keys()):
                ans += freq[x]
            return ans