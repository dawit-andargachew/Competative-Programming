class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # the question is Multi-source BFS.
        # Take each rotten oranges as if they are on the same level and make a BFs on them

        def isValid(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return False
            return True
        
        minute, q, initialOnes = 0, deque(), 0
        # It is multi Source BFS so take all 'rotten' oranges on the queue
        for r in range( len(grid)):
            for c in range( len(grid[0])):
                if grid[r][c] == 2:
                    q.append( [r,c] )
                if grid[r][c] == 1:
                    initialOnes += 1

        # calculate the time needed to rotten all oranges
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if isValid(newRow, newCol) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        q.append( [newRow, newCol])
                        initialOnes -= 1

            if len(q) > 0:
                minute += 1
        
        # After finishing BFS, initial fresh Oranges should be zero
        return minute if initialOnes == 0 else - 1