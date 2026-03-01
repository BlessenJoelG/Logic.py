class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for _ in words:
            if _ == _[::-1]:
                return(_)
                break
        return("")
