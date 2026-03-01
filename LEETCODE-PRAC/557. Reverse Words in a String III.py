class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for _ in range(len(s)):
            s[_] = s[_][::-1]
        return(" ".join(s))
