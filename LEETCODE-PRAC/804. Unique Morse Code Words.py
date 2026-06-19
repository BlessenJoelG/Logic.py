class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        translate,res= {},[]
        i,j = 97,0
        while(i<=122):
            translate[chr(i)] = morse[j]
            i += 1
            j += 1
        for word in words:
            code = ""
            for letter in word:
                code = code + translate.get(letter)
            if code not in res:
                res.append(code)
        return len(res)