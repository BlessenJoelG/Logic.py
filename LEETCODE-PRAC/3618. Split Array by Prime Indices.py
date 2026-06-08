class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prime = [True] * n
        if n > 0: prime[0] = False
        if n > 1: prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
        a = b = 0
        for i, x in enumerate(nums):
            if prime[i]:
                a += x
            else:
                b += x
        return abs(a - b)