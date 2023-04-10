class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0
        visited, directions = set(), [(0,1), (0,-1), (1,0), (-1,0)]

        def getFirstOne():
            startRow, startCol, row , col = 0, 0, 0, 0
            
            while row < len(grid):
                while col < len(grid[0]):
                    if grid[row][col] == 1:
                        startRow, startCol = row, col
                        row, col = len(grid), len(grid[0]) # breaks from the loop after getting the first one
                    col += 1
                col = 0 # reset column for the next row
                row += 1

            return [startRow, startCol]

        def isInValid(row, col):
            return row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0

        def dfs(row, col):
            nonlocal perimeter

            # base cases
            if isInValid(row, col) or grid[row][col] == 0:
                perimeter += 1
                return
            
            # calculate perimeter
            # for d in directions:
            #     newRow, newCol = row + d[0], col + d[1]
            #     if isInValid(newRow, newCol):
            #         perimeter += 1
            #     elif grid[newRow][newCol] == 0:
            #         perimeter += 1

            visited.add( ( row, col))
            for d in directions:
                newRow, newCol = row + d[0], col + d[1]
                if (newRow, newCol) not in visited:
                    dfs(newRow, newCol)

        # lets get the first 1 in the matrix and start find the perimeter over that
        startRow, startCol = getFirstOne()
        dfs(startRow, startCol)

        return perimeter