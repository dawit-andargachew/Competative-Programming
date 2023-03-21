# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # https://www.youtube.com/watch?v=sm4UdCO2868
        # To get the maximum width store each nodes index like this in dictinany
        # at each level store the left most position with its depth and in the next new depth caluclaute this
        # position - node-freq[depth] + 1 => this enable us to know 
        # the maximum width we can form from the left most to the right mos nodes we have visited so far

        max_width = 0
        node_freq = defaultdict(int)

        def solve( root, depth, position):
            nonlocal max_width

            if not root:
                return

            # track the left and right most depth with its respecitve position
            if depth not in node_freq:
                node_freq[depth] = position

            # update max_width relative to the current depth and position
            max_width = max(max_width, position - node_freq[depth] + 1 )

            solve( root.left, depth + 1, position * 2)
            solve( root.right, depth + 1, position * 2 + 1)
            
        solve(root, 0, 0)
        return max_width
        