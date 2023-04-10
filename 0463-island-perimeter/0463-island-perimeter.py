class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # perimeter = 0
        visited, directions = set(), [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(row, col):

            # base cases
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0

            visited.add( ( row, col))

            perimeter = 0
            for d in directions:
                newRow, newCol = row + d[0], col + d[1]
                perimeter += dfs(newRow, newCol)
            
            return perimeter
        
        # lets get the first 1 in the matrix and start find the perimeter over that
        for i in range( len(grid)):
            for j in range( len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)