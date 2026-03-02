class Solution:
    def isBalanced(self, num: str) -> bool:
        eve_idx_num,odd_idx_num = num[::2],num[1::2]
        eve_idx_num = [int(eve_idx_num[_]) for _ in range(len(eve_idx_num))]
        odd_idx_num = [int(odd_idx_num[_]) for _ in range(len(odd_idx_num))]
        if sum(eve_idx_num) == sum(odd_idx_num):
            return True
        else:
            return False
