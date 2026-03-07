class Solution:
    def numberOfMatches(self, n: int) -> int:
        tot_match = 0
        while(n>=2):
            if n%2 != 0:
                tot_match = tot_match + (n-1)/2
                n = ((n-1)/2)+1
            else:
                tot_match = tot_match + n/2
                n = n/2
        return int(tot_match)
