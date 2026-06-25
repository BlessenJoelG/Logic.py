class Solution:
    def sortSentence(self, s: str) -> str:
        freq,c = {},""
        for x in list(s.split(" ")):
            if x not in freq:
                freq[x[-1]] = x[:]
        for x in sorted(freq.keys()):
            c += freq[x]
        for i in range(len(c)):
            if i == len(c)-1:
                c = c.replace(c[i],"")
            elif c[i].isalpha() == False:
                c = c.replace(c[i]," ")
        return c