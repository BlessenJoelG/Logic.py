class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        tour,freq = {},{}
        for path in paths:
            for city in path:
                if city not in tour:
                    tour[city] = 1
                else:
                    tour[city] += 1
        for path in paths:
            freq[path[0]] = path[1]
        for x in freq.values():
            if tour.get(x) == 1:
                return x 