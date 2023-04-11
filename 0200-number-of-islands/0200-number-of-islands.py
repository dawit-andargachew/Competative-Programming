class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # similar with 695. Max Area of Island        
        visited = set()
        def dfs(row, col):            
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return
            if grid[row][col] == '0' or (row, col) in visited:
                return

            # store visited indices
            visited.add((row, col))

            # visite the maxtrix in dfs
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)        

        NumberOfIslands = 0
        for i in range(len(grid)):
            for j in range( len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i , j)
                    
                    #we got an Island, so update Numbe of Islands
                    NumberOfIslands += 1

                    # change visited '1' to '0', to prevent revisiting those again
                    for v in visited:
                        grid[ v[0] ][ v[1] ] = 0
                        
                    visited.clear() # clear visited and make it read for next dfs

        return NumberOfIslands