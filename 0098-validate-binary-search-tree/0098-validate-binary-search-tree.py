# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate( root, min_val, max_val):

            if not root:
                return True

            if not (root.val > min_val and root.val < max_val):
                return False

            left_valid = validate(root.left, min_val, root.val)
            right_valid = validate(root.right, root.val, max_val)

            return left_valid and right_valid

        return validate(root, float('-inf'), float('inf'))