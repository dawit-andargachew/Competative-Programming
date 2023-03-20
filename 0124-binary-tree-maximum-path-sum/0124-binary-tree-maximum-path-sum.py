# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # the path can't be split in to left or right, it needs to be a path without splitting
        # L-root-R or L-root-R-R-l-l etc. 
        # a given node can't have both left and right nodes, just one node only with maximum path sum
        max_sum = -2000

        def maximumPath(root):
            nonlocal max_sum

            if not root:
                return 0
            
            left = max(0, maximumPath(root.left))
            right = max(0, maximumPath(root.right))

            max_sum = max( max_sum, left + root.val + right)

            return root.val + max( left, right)

        maximumPath(root)

        
        return max_sum