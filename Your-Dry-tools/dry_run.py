class anagram:
    def chk_anagram(self,a,b):
        s = a
        t = b
        if sorted([x for x in s]) == sorted([x for x in t]):
            return True
        return False
Answer = anagram()
print(Answer.chk_anagram("anagram","nagaram"))