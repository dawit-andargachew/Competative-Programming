# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        counter = 0

        def buildTree(nums, upper_bound):
            nonlocal counter
            if counter == len(nums) or nums[counter] > upper_bound:
                return None
            node = TreeNode(nums[counter])
            counter += 1
            node.left = buildTree(nums, node.val)
            node.right = buildTree(nums, upper_bound)
            return node

        return buildTree(preorder, float("inf"))