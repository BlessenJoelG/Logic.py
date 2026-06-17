class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            a,b = set(A[:i+1]),set(B[:i+1])
            ans.append(len(a.intersection(b)))
        return ans