# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def path_sum(root, total):

            if not root:
                return
            
            if not root.left and not root.right:
                return total + root.val == targetSum
            
            left = path_sum(root.left, total + root.val)
            right = path_sum(root.right, total + root.val)

            return left or right
        
        return path_sum(root, 0)