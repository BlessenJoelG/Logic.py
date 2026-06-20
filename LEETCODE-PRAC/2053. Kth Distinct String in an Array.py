class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = []
        for x in arr:
            if arr.count(x) == 1:
                ans.append(x)
        if len(ans)<=k-1:
            return ""
        else:
            return ans[k-1]