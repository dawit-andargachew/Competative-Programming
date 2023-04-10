class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # Look at the other submissions too, from bad to better ...
        visited  = set()
        def dfs(row, col):
            # base cases
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0

            visited.add( ( row, col))

            perimeter = dfs(row, col)
            perimeter += dfs(row + 1, col)
            perimeter += dfs(row - 1, col)
            perimeter += dfs(row, col + 1)
            perimeter += dfs(row, col - 1)

            return perimeter
        
        # lets get the first 1 in the matrix and start find the perimeter over that
        for i in range( len(grid)):
            for j in range( len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)