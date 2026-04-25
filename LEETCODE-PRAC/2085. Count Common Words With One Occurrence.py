class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c = 0
        for x in words1:
            if words1.count(x) == 1 and words2.count(x) == 1 and x in words2:
                c += 1
        return c
