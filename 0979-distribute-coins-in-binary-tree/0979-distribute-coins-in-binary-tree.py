class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        
        def distubeCoins(root):
            if not root:
                return 0
            nonlocal result
            
            left = distubeCoins(root.left)
            right = distubeCoins(root.right)
            
            result += abs(left) + abs(right)
            
            return root.val + left + right - 1

        
        distubeCoins(root)
        
        return result
            