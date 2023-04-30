class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

     
        def isvalid(row, col):
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
                return True
            return False
        
        q, nearestExit, hasExit = deque(), 0, False

        q.append(entrance)
        maze[ entrance[0] ][ entrance[1] ] = "+"

        while q:
            
            size, count = len(q), 0
            for _ in range(size):
                row, col = q.popleft()
                for r, c in [ [0, 1], [0, -1], [1, 0], [-1, 0] ]:
                    newRow, newCol = row + r, col + c

                    if not isvalid(newRow, newCol) and nearestExit > 0:
                        return nearestExit

                    if isvalid(newRow, newCol) and maze[newRow][newCol] == ".":
                        q.append([newRow, newCol])
                        maze[newRow][newCol] = "+"

                    if not isvalid(newRow, newCol) and nearestExit > 0:
                        hasExit = True

            nearestExit += 1
        
        # if the maze has deadEnd or if is like Example-3 => return -1
        if nearestExit == 1 or not hasExit:
            return -1

        return nearestExit