# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        # to do this info, we need track two things
        # 1, level and 2, sum of each level
        # Lets store them in list [level, total_sum ], 
        # initialize it with the level 1 and total = root.val, because it helps to handle if there is only one node
        max_level_sum = [1, root.val]
        level = 0

        queue = deque()
        queue.append(root)
        
        while len(queue):
            
            width = len(queue)
            level += 1
            temp = []
            
            for i in range(width):
                
                if queue[0].left:
                    queue.append( queue[0].left )
                
                if queue[0].right:
                    queue.append( queue[0].right )
                
                temp.append( queue[0].val )
                queue.popleft()
            
            total = sum(temp)
            # if total > max_level_sum[1], update both level and total sum
            if max_level_sum[1] < total:
                max_level_sum[0] = level
                max_level_sum[1] = total
        
        return max_level_sum[0]