class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            ans = sorted(nums[l[i]:r[i]+1])
            k = abs(ans[0]-ans[1])
            val = True
            for j in range(len(ans)-1):
                if abs(ans[j]-ans[j+1]) != k:
                    val = False
                    break
            res.append(val)
        return res