# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # in here apply breath first search and return the values located on the last
        # so that they can be seen by the person standing to the right side of it
        if not root:
            return []
        
        level_order = []
        q = deque()
        q.append( root )

        while q:
            current_width = []
            length = len(q)

            for i in range(length):

                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append( q[0].right )
                
                current_width.append( q.popleft().val )
                
            # always append the last element after traversing nodes on the same level
            level_order.append( current_width[-1] )

        return level_order