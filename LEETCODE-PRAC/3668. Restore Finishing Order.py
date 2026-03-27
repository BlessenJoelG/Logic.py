class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        final_list = []
        for x in order:
            if x in friends:
                final_list.append(x)
        return(final_list)  
