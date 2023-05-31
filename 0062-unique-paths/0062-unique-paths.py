class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [ [0 for i in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = 1

        def DP_func(row, col):
            if 0 <= row < m and 0 <= col < n:
                return dp[row][col]
            return 0

        # bottom up approach, starting from target.
        for r in range(m):
            for c in range(n):
                row, col = m - r - 1, n - c - 1
                dp[row][col] += DP_func(row, col + 1) + DP_func(row + 1, col)
            
        return dp[0][0]