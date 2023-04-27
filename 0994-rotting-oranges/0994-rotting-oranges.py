class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # the question is Multi-source BFS.
        # Take each rotten oranges as if they are on the same level and make a BFs on them

        def isValid(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return False
            return True
        
        time, visited, q, initialOnes, finalOnes = 0, set(), deque(), 0, 0
        # It is multi Source BFS so take all 'rotten' oranges on the queue
        for r in range( len(grid)):
            for c in range( len(grid[0])):
                if grid[r][c] == 2:
                    q.append( [r,c] )
                    visited.add( (r,c) )
                if grid[r][c] == 1:
                    initialOnes += 1

        # calculate the time needed to rotten all oranges
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            size, FreshOrangeOnThisLevel = len(q), 0
            for _ in range(size):
                row, col = q.popleft()
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if (newRow, newCol) not in visited and isValid(newRow, newCol) and grid[newRow][newCol] == 1:
                        q.append( [newRow, newCol])
                        visited.add( (newRow, newCol))
                        FreshOrangeOnThisLevel, finalOnes = FreshOrangeOnThisLevel + 1, finalOnes + 1

            if FreshOrangeOnThisLevel > 0:
                time += 1
        
        # After finishing BFS, initial and final fresh Oranges should be the same
        return time if initialOnes == finalOnes else - 1