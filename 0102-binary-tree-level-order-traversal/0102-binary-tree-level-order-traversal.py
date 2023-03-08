# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return 

        returned_list = []
        queue = deque()
        
        queue.append(root)
        
        while len(queue):
            
            width = len(queue)
            temp = []
            
            for i in range(width):
                
                if queue[0].left:
                    queue.append( queue[0].left )
                
                if queue[0].right:
                    queue.append( queue[0].right )
                
                temp.append( queue[0].val )
                queue.popleft()
            
            returned_list.append( temp )
        
        return returned_list