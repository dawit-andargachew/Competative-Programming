# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        counter = 0
        freq = {}
        
        # store the frequency of each element and max frequency
        def traverse(root):
            nonlocal counter
            
            if root:
                
                traverse(root.left)
                
                freq[root.val] = freq.get(root.val, 0) + 1
                counter = max(counter, freq.get(root.val) )   
                
                traverse(root.right)
        
        traverse(root)
        
        modes = []
        # extract elements which have max frequency
        for i in freq:
            if freq.get(i) == counter:
                modes.append(i)
        
        return modes