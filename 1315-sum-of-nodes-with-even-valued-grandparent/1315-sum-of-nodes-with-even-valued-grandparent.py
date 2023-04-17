# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        # if current node parent is even, add its children and return their sum
        def dfs(root, val):
            if not root:
                return 0
            
            answer = 0
            if val % 2 == 0:
                if root.left:
                    answer += root.left.val
                if root.right:
                    answer += root.right.val

            return answer + dfs(root.left, root.val) + dfs(root.right, root.val)

        
        return dfs(root.left, root.val) + dfs(root.right, root.val)