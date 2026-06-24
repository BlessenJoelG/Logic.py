class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        freq1,freq2,ans = {},{},[]
        for x in items1:
            freq1[x[0]] = x[1]
        for x in items2:
            freq2[x[0]] = x[1]
        for x in freq1.keys():
            if x in freq2:
                ans.append([x,freq1[x]+freq2[x]])
            else:
                ans.append([x,freq1[x]])
        for x in freq2.keys():
            if x not in freq1:
                ans.append([x,freq2[x]])
        return sorted(ans)