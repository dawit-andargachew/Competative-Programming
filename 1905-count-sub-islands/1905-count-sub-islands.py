class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        # similar with 695. Max Area of Island        
        visited = set()
        def dfs(row, col):            
            if row >= len(grid2) or row < 0 or col >= len(grid2[0]) or col < 0:
                return
            if grid2[row][col] == 0 or (row, col) in visited:
                return

            # store visited indices
            visited.add((row, col))

            # visite the maxtrix in dfs
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)        

        # makes sure the Island on graph2 is sub-island on graph1
        def isSubIsland():            
            for v in visited:
                if grid1[ v[0] ][ v[1] ] != grid2[ v[0] ][ v[1] ]:
                    return False
            return True

        Sub_Islands = 0
        for i in range(len(grid2)):
            for j in range( len(grid2[0])):
                if grid2[i][j] == 1:
                    dfs(i , j)
                    
                    #we got an Island, so update Numbe of Islands
                    if isSubIsland():
                        Sub_Islands += 1

                    # change visited '1' to '0', to prevent revisiting those again
                    for v in visited:
                        grid2[ v[0] ][ v[1] ] = 0
                        
                    visited.clear() # clear visited and make it read for next dfs

        return Sub_Islands