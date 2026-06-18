class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        grp,ans = {},[]
        for i in range(len(groupSizes)):
            if groupSizes[i] not in grp:
                grp[groupSizes[i]] = [i]
            else:
                grp[groupSizes[i]].append(i)
        for size,people in grp.items():
            for i in range(0,len(people),size):
                ans.append(people[i:i+size])
        return ans