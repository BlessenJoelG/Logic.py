class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        s,str_itr,c = [x for x in s],"",0
        for x in s:
            str_itr = str_itr + x
            y = str_itr
            for _ in words:
                if y == _:
                    c = c + 1
        return(c)
