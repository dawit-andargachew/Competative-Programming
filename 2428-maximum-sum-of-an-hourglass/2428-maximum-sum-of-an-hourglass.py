class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        row, col = len(grid) - 2, len(grid[0]) - 2
        max_sum = 0

        for r in range(row):

            for c in range(col):
                curr = 0

                for i in range(3):
                    for j in range(3):
                        curr += grid[r + i][c + j]
                curr -= ( grid[r + 1][c] + grid[r + 1][c + 2])
                
                max_sum = max( max_sum, curr)

        return max_sum