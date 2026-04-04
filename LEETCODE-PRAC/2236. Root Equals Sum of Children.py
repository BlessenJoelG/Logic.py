#my first binarytree category leetcode question
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        roots = root.val
        root_left = root.left.val
        root_right = root.right.val
        if (roots == (root_left+root_right)):
            return True
        else:
            return False