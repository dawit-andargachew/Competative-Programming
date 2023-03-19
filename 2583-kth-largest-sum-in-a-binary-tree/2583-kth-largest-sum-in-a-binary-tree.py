# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        q = deque()
        q.append( root)

        # store every level sum in array, sort them and return kth largest sum,
        # total_sum [ len(total_sum) - k ] is kth largest total sum
        total_sum = []
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

            total_sum.append( sum(temp) )

        total_sum.sort()

        if k <= len(total_sum):
            return total_sum[ len(total_sum) - k]
        else:
            return -1
