class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
       costs.sort()
       c = 0
       for price in costs:
            if price<=coins:
                coins -= price
                c += 1
            else:
                break
       return c