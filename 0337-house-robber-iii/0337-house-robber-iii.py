class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Define the helper function
        def dfs(node):
            if not node:
                return (0, 0)
            
            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)
            
            rob_this = node.val + left_not_rob + right_not_rob
            not_rob_this = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
            
            return (rob_this, not_rob_this)
        
        return max(dfs(root))