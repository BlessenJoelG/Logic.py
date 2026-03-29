class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for x in accounts:
            wealth.append(sum(x))
        return max(wealth)