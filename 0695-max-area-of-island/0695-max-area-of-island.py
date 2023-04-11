class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        def dfs(row, col):
            
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return

            if grid[row][col] == 0 or (row, col) in visited:
                return

            visited.add((row, col)) # store visited indices

            # visite the maxtrix in dfs
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        

        maxArea = 0
        for i in range(len(grid)):
            for j in range( len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i , j)
                    
                    # area of island is the same as len(visited), so update the maxArea
                    maxArea = max(maxArea, len(visited))

                    # change visited '1' to '0', to prevent revisiting those again
                    for v in visited:
                        grid[ v[0] ][ v[1] ] = 0
                        
                    visited.clear() # clear visited and make it read for next dfs

        return maxArea