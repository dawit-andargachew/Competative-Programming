# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        column_value_map = defaultdict(list)
        result = []

        def traverse(root, row, col):
            if root == None:
                return

            traverse(root.left, row + 1, col - 1)

            column_value_map[col].append([row, root.val])

            traverse(root.right, row + 1, col + 1)

        traverse(root, 0, 0)

        
        myKeys = list(column_value_map.keys())
        myKeys.sort()

        for key in myKeys:
            temp = column_value_map[key]
            temp.sort()
            values = []
            
            for val in temp:
                values.append(val[1])

            result.append(values)
            
        return result