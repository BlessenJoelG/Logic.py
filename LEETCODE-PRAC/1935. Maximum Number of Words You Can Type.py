class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text,ans = text.split(" "),0
        brokenletters = [x for x in brokenLetters]
        for word in text:
            for letter in brokenLetters:
                if word.count(letter)>0:
                    ans = ans + 1
                    break
        return (len(text)-ans)