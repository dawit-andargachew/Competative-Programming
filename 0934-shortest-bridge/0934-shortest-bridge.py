class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        # The solution to this problem is,
        # step - 1: get all the components of Island 1
        # step - 2: treate Island one components as if there are on the same level 
        #           and make BFS until we get Island 2
        # -> so the number of moves until we get Island 2 is SHORTEST BRIDGE

        # step-1, get all components of island 1
        islandOne, q, visited = deque(), deque(), set()
        for r in range( len(grid)):
            for c in range( len(grid[0])):
                if grid[r][c] == 1:
                    islandOne.append([r, c])
                    q.append([r, c])
                    visited.add((r,c))
                    break
            if len(islandOne) == 1:
                break
        
        def isvalid(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid):
                return True
            return False

        # make a BFS on the first land cell and get all cell in Islandone
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                for r, c in [ [0, 1], [0, -1], [1, 0], [-1, 0]]:
                    newRow, newCol = row + r, col + c
                    if (newRow,newCol) not in visited and isvalid(newRow, newCol) and grid[newRow][newCol] == 1:
                        q.append([newRow, newCol])
                        islandOne.append([newRow, newCol])
                        visited.add((newRow, newCol))
        
        # step-2, make BFS on islandOne until we get Island-2
        bridge = 0
        while islandOne:
            size = len(islandOne)
            for _ in range( size ):
                row, col = islandOne.popleft()
                for r, c in [[0, 1],[0, -1],[1, 0], [-1, 0]]:
                    newRow, newCol = row + r, col + c

                    if (newRow,newCol) not in visited and isvalid(newRow, newCol):
                        # there are exactly 2 islands, so terminate here since Island-2 is found
                        if grid[newRow][newCol] == 1:
                            return bridge

                        islandOne.append([newRow, newCol])
                        visited.add((newRow, newCol))
            bridge += 1