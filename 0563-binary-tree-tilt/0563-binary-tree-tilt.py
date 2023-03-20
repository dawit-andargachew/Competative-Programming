# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:


        tilt_sum = 0
        
        # everyparent node wants its left and right sub tree sum,
        # and at the same time tilt_sum should be updated by their absolute difference
        def solve(root):
            nonlocal tilt_sum

            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)

            tilt_sum += abs(left - right)

            return left + right + root.val

        solve(root)

        return tilt_sum