# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        s_string = ""
        acc = []

        def smallest_leaf(root):
            nonlocal s_string

            if not root:
                return
            
            #store every visted node, and decode each value in to a letter
            acc.append( self.letters [root.val])

            # everytime leaf node is visited, update lexicographically smallest string
            if not root.left and not root.right:

                if s_string == "":
                    s_string = ''.join(acc[::-1])
                else:

                    temp = ''.join(acc[::-1])
                    s_string = min(s_string, temp)


            smallest_leaf(root.left)
            smallest_leaf(root.right)

            # remove node after visiting left and right 
            acc.pop()
        
        
        smallest_leaf(root)

        return s_string