# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        kth_num = 0
        counter = 0
        
        # keep track of the coutner and grap the number when counter equals k
        def inorder_(root):
            nonlocal counter
            nonlocal kth_num
            
            if root:

                inorder_(root.left)
                counter += 1
                if counter == k:
                    kth_num = root.val
                    return

                inorder_( root.right)
        
        inorder_(root)

        return kth_num