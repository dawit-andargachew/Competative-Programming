class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        answer = []
        row, col = len(grid) - 2, len( grid[0]) - 2

        for r in range(row):

            temp = []# store max elements which are on the same row of the final answer
            for c in range(col):

                maxLocal = grid[r][c] # store max element on tehe 3 * 3 grid
                for i in range(3):
                    for j in range(3):
                        maxLocal = max(maxLocal, grid[r+i][c+j])
                temp.append(maxLocal)

            answer.append( temp[:] )
        
        return answer