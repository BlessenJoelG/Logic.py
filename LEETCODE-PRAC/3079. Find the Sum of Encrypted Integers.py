class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = []
        for x in (nums):
            x = str(x)
            res.append(int(len(x)*str(max([int(i) for i in x]))))
        return(sum(res))