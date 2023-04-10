class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(row, col):
            
            # base case
            if row >= len(image) or col >= len(image[0]) or row < 0 or col < 0:
                return

            if image[row][col] != image[sr][sc]:
                return

            visited.add( (row, col))
            for d in directions:
                newRow, newCol = row + d[0], col + d[1]
                if (newRow, newCol) not in visited:
                    dfs(newRow, newCol)
        
        dfs(sr, sc)

        # change each
        for v in visited:
            image[v[0]][v[1]] = color
    
        return image