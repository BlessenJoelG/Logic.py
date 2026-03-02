class Solution:
    def isAcronym(self, words, s) -> bool:
        acro = ""
        for _ in words:
            acro = acro + _[0]
        if acro == s:
            return True
        else:
            return False
