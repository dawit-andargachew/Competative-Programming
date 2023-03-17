# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:

        if not root:
            return 0

        total = 0
        map = defaultdict(int)
        map[0] = 1

        def solution(root, prefix_s):
            nonlocal total

            if not root:
                return

            prefix_s += root.val
            if (prefix_s - target) in map:
                total += map[ (prefix_s - target) ]
            map[ prefix_s ] += 1


            # call left
            solution(root.left, prefix_s)
            # call right
            solution(root.right, prefix_s )
            
            # after travesing left and right subtree, remove the current prefix sum in the map
            # Preorder traversal visit first left then right, so
            #  first visit left
            #  then visit right 
            #  remove  the prefix_sum on map
            map[ prefix_s ] -= 1
            if map[prefix_s] == 0:
                map.pop(prefix_s)
        
        solution(root, 0)

        return total



        