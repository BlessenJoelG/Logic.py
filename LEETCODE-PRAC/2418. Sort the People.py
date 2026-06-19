class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tall,ans = {},[]
        for i in range(len(heights)):
            if heights[i] not in tall:
                tall[heights[i]] = names[i]
        heights.sort(reverse = True)
        for i in heights:
            ans.append(tall.get(i))
        return ans