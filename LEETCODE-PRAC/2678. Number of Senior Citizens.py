class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        details = [int(x[11:13]) for x in details]
        for age in details:
            if age > 60:
                c = c + 1
        return c
