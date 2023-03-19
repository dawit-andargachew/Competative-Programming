# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        # store each level traversal nodes
        level_order = []
        q = deque()

        q.append( root )

        while q:
            width = len(q)
            temp = []
            for i in range(width):
                if q[0].left:
                    q.append( q[0].left )
                if q[0].right:
                    q.append( q[0].right )
                
                temp.append( q[0].val )
                q.popleft()

            level_order.append(temp)

            
        # return in reverse order
        return level_order[::-1]