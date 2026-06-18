class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
       freq,res = {},[]
       for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
       for i in range(max(freq.values())):
            ans = []
            for num,times in freq.items():
                if times>0:
                    ans.append(num)
                    freq[num] -= 1
            res.append(ans)
       return res