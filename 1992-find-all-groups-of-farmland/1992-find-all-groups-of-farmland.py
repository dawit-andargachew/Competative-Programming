class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        # similar with 695. Max Area of Island  
        #              1905. Count Sub Islands
        #              695. Max Area of Island
        visited = set()
        def dfs(row, col, edges):            
            if row >= len(land) or row < 0 or col >= len(land[0]) or col < 0:
                return edges
            if land[row][col] == 0 or (row, col) in visited:
                return edges

            # store visited indices
            visited.add((row, col))
            
            # for every move lets check the top-left and bottom-right edges
            # for top left
            if edges[0] > row or edges[1] >col:
                edges[0], edges[1] = row, col            
            # for bottom right
            if edges[2] < row or edges[3] < col:
                edges[2], edges[3] = row, col
            

            # visite the maxtrix in dfs
            dfs(row + 1, col, edges)
            dfs(row - 1, col, edges)
            dfs(row, col + 1, edges)
            dfs(row, col - 1, edges)    

            return edges

        coordinates = []
        for i in range(len(land)):
            for j in range( len(land[0])):
                if land[i][j] == 1 and (i, j):
                    
                    # append the edges to the coordinates
                    edges = dfs(i , j, [i, j, i, j])
                    coordinates.append( edges)
                    
                    # change visited '1' to '0', to prevent revisiting those again
                    for v in visited:
                        land[ v[0] ][ v[1] ] = 0
                        
                    visited.clear() # clear visited and make it read for next dfs
        return coordinates