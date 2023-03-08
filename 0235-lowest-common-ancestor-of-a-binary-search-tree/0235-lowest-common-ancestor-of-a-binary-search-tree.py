# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        stack1 = []
        stack2 = []
        def search_func_(root, key, stack):

            if not root:
                return
            elif root.val == key:
                stack.append(root)
                return

            elif root.val > key:
                stack.append(root)
                return search_func_(root.left, key, stack)

            elif root.val < key:
                stack.append(root)
                return search_func_(root.right, key, stack)

        search_func_(root, p.val, stack1)
        search_func_(root, q.val, stack2)

        common_ancestor = None
        
        for i in range( min( len(stack1), len(stack2))):
            if stack1[i] == stack2[i]:
                common_ancestor = stack1[i]


        return common_ancestor