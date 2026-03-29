class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        leftsum,rightsum = [],[]
        for i in range(len(nums)):
            if i == 0:
                leftsum.append(0)
            else:
                leftsum.append(sum(nums[:i]))
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                rightsum.append(0)
            else:
                rightsum.append(sum(nums[:i:-1]))
        rightsum = rightsum[::-1]
        for _ in range(len(nums)):
            answer.append(abs(leftsum[_]-rightsum[_]))
        return answer