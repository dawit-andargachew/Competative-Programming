# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:


        q  = deque()
        q.append( root )

        deepest_level = 0

        # iterate over each level, and update deepest_level until the deepest level,
        # when we reach the deepest level, deepest_level will be deepest level sum
        while q:
            width = len(q)
            
            temp = 0
            for _ in range( width):
                if q[0].left:
                    q.append( q[0].left )

                if q[0].right:
                    q.append( q[0].right )
                
                temp += q[0].val
                q.popleft()
                deepest_level = temp
            
        return deepest_level