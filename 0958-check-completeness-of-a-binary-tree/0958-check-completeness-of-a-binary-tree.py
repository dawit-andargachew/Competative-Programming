# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    
        # ITERATIVE SOLUTION
        # when ever we get a null node, everything after that should be null
        # It can be done by Breadth first seach
        q = deque()
        q.append(root)

        while q:
            temp = q.popleft()
            if temp:
                q.append(temp.left)
                q.append(temp.right)
            
            # whenever a null node occurs, everynode after that should be null
            # if there is none null node, return False
            else:
                while q:
                    if q.popleft():
                        return False
        
        return True

 

# # RECURSIVE SOLUTION
# class Solution:
#     def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
#         # a complete binary tree is filled from left to right, so each node needs two things
#         # 1, does the left and right sub-tree are complete
#         # 2, left shallowest and right deepest nodes should differ at most by one
#         # meaning,
#         #       left - right <= 1 and left >= right => so we can say it is definately complete binary tree

#         # each node returns three things
#         # [is_sub_tree_complete, deepest, shallowet]

#         def check_complete(root):
            
#             # [ is_complete, deepest, shallow]
#             if not root:
#                 return [True, 0, 0]
            
#             if not root.left and not root.right:
#                 return [True, 1, 1]
            
#             left = check_complete(root.left)
#             right = check_complete(root.right)

#             is_complete = left[0] and right[0] and left[2] >= right[1] and ( left[2] - right[1] <= 1 )
#             max_depth = max(left[1], right[1]) + 1
#             min_depth = min(left[2], right[2]) + 1 

#             return [is_complete,max_depth, min_depth]

#         result = check_complete(root)

#         return result[0] and result[1] - result[2] <= 1