class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted([x for x in s]) == sorted([x for x in t]):
            return True
        return False