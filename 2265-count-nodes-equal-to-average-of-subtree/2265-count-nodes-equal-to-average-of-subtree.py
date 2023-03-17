# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        averages = 0
        
        # everyNode needs two things,
        # 1, left subtree total and numbers
        # 2, right subtree total and numbers

        def solution(root):
            nonlocal averages
            
            # null, return 0, 0 => sum = 0 and total = 0
            if not root:
                return 0, 0
            

            left = solution(root.left)
            right = solution(root.right)
            val = root.val

            # total = left + right +  val
            total = left[0] + right[0] + root.val

            # n of values = left + right + 1, 1 for current node
            n = left[1] + right[1] + 1

            if total//n  == val:
                averages += 1

            return total, n
        
        solution(root)

        return averages