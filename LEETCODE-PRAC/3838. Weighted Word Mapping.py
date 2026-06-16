class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        w,f = {},{}
        i,j = 97,0
        while(i<=122):
            w[chr(i)] = weights[j]
            i += 1
            j += 1
        i,j = 122,0
        while(i>=97):
            f[j] = chr(i)
            i -= 1
            j += 1
        ans = ""
        for word in words:
            ans = ans + f.get((sum(w[x] for x in word))%26)
        return ans  