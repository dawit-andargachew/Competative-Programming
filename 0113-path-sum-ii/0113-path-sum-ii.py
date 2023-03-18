# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        answer = []
        acc = []

        def solve(root, total):
            
            if not root:
                return
            
            # store total and keep track of each value visited
            total += root.val
            acc.append(root.val)

            if not root.left and not root.right:

                # check total in leaf nodes and append to answer
                if total == targetSum:
                    answer.append(acc[:])
            

            solve(root.left, total)
            solve(root.right, total)

            # remove the last visited node after traversing left and right nodes
            acc.pop()
        
        solve(root, 0)
        return answer
        