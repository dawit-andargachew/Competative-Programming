# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        acc = []

        def leaf_numbers(root):
            nonlocal answer

            if not root:
                return
            
            # record each root.val visited
            acc.append(root.val)

            # for leaf nodes, add the number to the global variable
            if not root.left and not root.right:

                number = 0
                size = len(acc) - 1

                # change to number
                for i in range( len(acc) ):
                    number += acc[ size - i] * 10**i
                
                answer += number
            
            leaf_numbers(root.left)
            leaf_numbers(root.right)
            
            # remove last visited node after traversing left and right nodes
            acc.pop()

        leaf_numbers(root)

        return answer