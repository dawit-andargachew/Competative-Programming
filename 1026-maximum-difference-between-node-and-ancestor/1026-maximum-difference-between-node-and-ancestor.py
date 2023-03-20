# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        max_diff = -1

        # to get the max difference each parent node needs two things
        # 1, the lowest value in the sub-tree
        # 2, the highest value in the sub-tree
        # ane every node returns [ lowest_value, highest_value ]
        def solve(root):
            nonlocal max_diff

            # [ min_value, max_value ]
            if not root.left and not root.right:
                return [root.val, root.val]

            left = solve(root.left) if root.left else [root.val, root.val]
            right = solve(root.right) if root.right else [root.val, root.val]
        
            # extreact the lowest and hihgest value 
            max_value =max( left[0], left[1], right[0], right[1], root.val )
            min_value =  min( left[0], left[1], right[0], right[1], root.val )

            # update the maximum difference if there is any
            max_diff = max( max_diff, abs(min_value - root.val), abs(max_value - root.val))

            # return the [ min_value, max_value ] to the preceding parent node
            return [min_value, max_value]

        solve(root)
        
        return max_diff