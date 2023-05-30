class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

#         def dp(n):
#             if n <= 1:
#                 return cost[n]
#             return cost[n] + min( dp(n - 1), dp(n - 2))
        # size = len(cost)
#         return min( dp( size - 1 ), dp( size - 2 ))
        
        size = len(cost)
        memo = [0] * ( size + 1 )

        for i in range(2, size + 1):
            memo[i] = min(cost[i - 1] + memo[i - 1], cost[i - 2] + memo[i - 2])

        return memo[-1]
