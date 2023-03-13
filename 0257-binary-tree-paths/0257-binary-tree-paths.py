# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        accu = []

        def backtrack(node):
            if not node:
                return

            if not node.left and not node.right:
                path = ''.join(accu) + str(node.val)
                ans.append(path)
                return
                

            if node:
                accu.append(str(node.val) + "->")
                backtrack(node.left)

                backtrack(node.right)
                accu.pop()

        backtrack(root)

        return ans