class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # edge cases
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1 and grid[0][0] == 0:
            return 1

        def isvalid(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return False
            return True

        q = deque()
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1]]
        target = [len(grid)-1, len(grid[0]) - 1]

        q.append([0,0])
        minPath = 1 # lets cosider the current node

        while q:

            minPath += 1
            size = len(q)
            for _ in range(size):

                row, col = q. popleft()
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if isvalid(newRow, newCol) and grid[newRow][newCol] == 0:
                        
                        grid[newRow][newCol] = 1 # mark the grid to 1 and consider it as visited
                        
                        # if the target is reached return the path
                        if target == [newRow, newCol]:
                            return minPath

                        q.append( [newRow, newCol])
            
        return -1