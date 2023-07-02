class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        visited, area = set(), 0
        def isValid(row, col):
            nonlocal area
            if 0 <= row < len(grid) and 0<= col < len(grid[0]) and grid[row][col] == 1:
                return True
            else:
                area += 1
    
        def dfs(row, col):
            visited.add((row, col))
            for r, c in [ [0, 1], [1, 0], [0, -1], [-1, 0]]:
                newRow, newCol = row + r, col + c
                if isValid(newRow, newCol) and (newRow, newCol) not in visited:
                    dfs(newRow, newCol)

        isFound = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    isFound = True
                    dfs(i, j)
                    break # break inner loop
                
            if isFound: # break outer loop
                break

        return area