class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
       chk,c = {x for x in word.lower()},0
       for x in chk:
            if (x.lower() in word) and (x.upper() in word):
                c += 1
       return c 