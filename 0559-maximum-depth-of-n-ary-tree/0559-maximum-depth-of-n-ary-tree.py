"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def DFS_traversal( root ):
            if not root:
                return 0

            depth = 0
            # iterate over each nodes ad return depth + 1 => including the current node
            for child in root.children:                
                depth = max( DFS_traversal( child ), depth)
            
            return depth + 1

        return DFS_traversal( root )