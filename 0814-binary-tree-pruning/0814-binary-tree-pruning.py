# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # every child returns wheather it is 0 0r 1, depending on it parent decides to remove or not
        def remove(root):

            if not root:
                return

            left = remove(root.left)
            right = remove( root.right )

            if not left:
                root.left = None
            if not right:
                root.right = None
            return left or right or root.val == 1

        result = remove(root)

        # if the root node after removal is 0, return None
        if not result:
            return None
        else:
            return root