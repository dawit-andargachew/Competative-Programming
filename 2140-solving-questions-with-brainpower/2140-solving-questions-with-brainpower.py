class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:

        # here a dp problem similar to 198. House Robber
        n = len(q)
        dp = [-1] * n

        def helper(ind):
            if ind == (n - 1):
                return q[-1][0]
            if ind >= n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            
            nottake = helper(ind + 1)
            take = q[ind][0] + helper(ind + q[ind][1] + 1)
            dp[ind] = max(take, nottake)
            return dp[ind]

        return helper(0)