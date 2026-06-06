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
    
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls,rs,res =[],[],[]
        for i in range(len(nums)):
            ls.append(sum(nums[:i]))
        nums = nums[::-1]
        for i in range(len(nums)):
            rs.append(sum(nums[:i]))
        rs = rs[::-1]
        for i in range(len(nums)):
            res.append(abs(ls[i]-rs[i]))
        return res