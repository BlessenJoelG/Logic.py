class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        ans.append(first)
        for _ in range(len(encoded)):
            ans.append(ans[_]^encoded[_])
        return(ans)