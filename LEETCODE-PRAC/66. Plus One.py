class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tot = ""
        for x in digits:
            tot = tot + str(x)
        tot = str(int(tot)+1)
        digits = [int(x) for x in tot]
        return digits