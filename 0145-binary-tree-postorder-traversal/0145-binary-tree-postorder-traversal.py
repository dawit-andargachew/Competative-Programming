# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        element = []
        
        def postOrder(root):
            if not root:
                return
            postOrder(root.left)
            postOrder(root.right)
            element.append(root.val)
        
        postOrder(root)
        
        return element
            
        