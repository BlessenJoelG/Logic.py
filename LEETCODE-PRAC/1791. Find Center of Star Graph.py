class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        lst = []
        for x in edges:
            lst.extend(x)
        for _ in lst:
            if lst.count(_) == len(edges):
                return _
                break