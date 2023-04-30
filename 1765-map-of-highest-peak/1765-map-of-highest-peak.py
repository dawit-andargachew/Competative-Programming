class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        # here is just a simple BFS traversal questions
        visited, q = set(), deque()
        for r in range( len(isWater) ):
            for c in range( len(isWater[0]) ):
                if isWater[r][c] == 1:
                    isWater[r][c] = 0
                    q.append( [r,c] )
                    visited.add((r,c))

        def isvalid(row, col):
            if 0 <= row < len(isWater) and 0 <= col < len(isWater[0]):
                return True
            return False

        level = 1
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                for r, c in [ [0, 1], [0 ,-1], [1, 0], [-1, 0]]:
                    newRow, newCol = row + r, col + c
                    if (newRow, newCol) not in visited and isvalid(newRow, newCol):
                        isWater[newRow][newCol] = level
                        q.append([newRow, newCol])
                        visited.add((newRow, newCol))
            level += 1

        return isWater