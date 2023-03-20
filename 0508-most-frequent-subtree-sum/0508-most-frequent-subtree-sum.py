# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        map = defaultdict(int)

        # it is the same as 563. Binary Tree Tilt
        # in each node 
        #  - update map, by adding the sub tree sum on it
        #  - and return the sub tree sum to its parent
        def solve(root):

            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)

            sub_tree_sum = left + right + root.val

            # update map 
            map[sub_tree_sum] +=1
            
            # return to its parent
            return sub_tree_sum
        
        solve(root)

        # get the most frequent sum
        most_freq = max(map.values())

        # extract elements which have most_freq frequency
        nums = []
        for i in map:
            if map[i] == most_freq:
                nums.append( i )

        return nums