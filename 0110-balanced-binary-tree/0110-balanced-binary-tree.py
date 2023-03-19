# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        # to check wheather it is balanced or not, 
        # check every sub-tree from buttom to top approach by calling recursively
        # And each parent node needs two things from its child
        # 1, their height
        # 2, weather they are balnced or not
        # so return this info to there respective parents unil we reach root node
        
        def validate(root, level):

            if not root:
                return [level, True]

            if not root.left and not root.right:
                return [level + 1, True]

            
            left = validate(root.left, level + 1)
            right = validate(root.right, level + 1)

            return [max(left[0], right[0]), left[1] and right[1] and abs(left[0] - right[0]) <= 1]


        return validate(root, 0)[1]