# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        def validate_flip(root1, root2):

            if not root1 and not root2:
                return True
            
            if not root1 and root2 or root1 and not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            a = validate_flip(root1.left, root2.right) and validate_flip(root1.right, root2.left)
            b = validate_flip(root1.left, root2.left) and validate_flip(root1.right, root2.right) 

            return a or b

        return validate_flip(root1, root2)