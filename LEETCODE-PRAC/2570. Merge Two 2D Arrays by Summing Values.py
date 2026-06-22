class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        freq,res = {},[]
        for x in nums1:
            if x[0] not in freq:
                freq[x[0]] = x[1]
        for x in nums2:
            if x[0] not in freq:
                freq[x[0]] = x[1]
            else:
                freq[x[0]] += x[1]
        for x in freq.items():
            res.append(list(x))
        return sorted(res)