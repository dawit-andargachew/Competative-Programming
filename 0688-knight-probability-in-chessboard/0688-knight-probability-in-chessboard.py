class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2) ]

        # Dynamic Programming
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1

        for dk in range(k):
            temp_dp = [[0 for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    if dp[i][j] == 0:
                        continue
                    for x, y in directions:
                        delta_x, delta_y = i + x, j + y
                        if 0 <= delta_x < n and 0 <= delta_y < n:
                            temp_dp[delta_x][delta_y] += dp[i][j] / 8
            dp = temp_dp
        return sum([sum(l) for l in dp])