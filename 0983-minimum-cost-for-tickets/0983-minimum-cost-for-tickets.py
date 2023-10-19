class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = dict()

        def solve(i, m):
            if i == n:
                return 0
            if m >= days[i]:
                return solve(i + 1, m)

            if i in dp:
                return dp[i]
            dp[i] = min(
                [
                    costs[0] + solve(i + 1, days[i]),
                    costs[1] + solve(i + 1, days[i] + 6),
                    costs[2] + solve(i + 1, days[i] + 29),
                ]
            )
            return dp[i]

        return solve(0, 0)
