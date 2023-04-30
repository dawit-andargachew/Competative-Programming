class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        # This question just simply multi source BFS, 
        # take every land as if there are on the same level and return the max level

        visited, q = set(), deque()
        for r in range( len(grid) ):
            for c in range( len(grid[0]) ):
                if grid[r][c] == 1:
                    q.append( [r, c] )
                    visited.add( (r, c) )
        
        # edge case, no land or no water => return -1
        if len(q) == 0 or len(q) == len(grid) ** 2:
            return -1        

        def isvalid(row, col):
            if 0 <= row < len(grid) and 0 <=  col < len(grid):
                return True
            return False

        level, directions = 0, [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if (newRow, newCol) not in visited and isvalid(newRow, newCol):
                        q.append([newRow, newCol])
                        visited.add((newRow, newCol))
            level += 1

        return level - 1