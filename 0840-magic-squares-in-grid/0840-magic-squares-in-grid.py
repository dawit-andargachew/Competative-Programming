class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        row, col = len(grid) - 2, len(grid[0]) - 2
        magicSquares = 0

        for r in range(row):

            for c in range(col):
                diagonal1, diagonal2 = 0, 0
                col1, col2, col3 = 0, 0, 0
                row1, row2, row3 = 0, 0, 0
                are_unique = set()

                for i in range(3):
                    for j in range(3):
                        
                        # count the numbers and make sure they are in the range 1 to 9
                        if grid[r + i][c + j] <= 9 and grid[r + i][c + j] > 0 :
                            are_unique.add( grid[r + i][c + j] )
                        else:
                            break

                        # for column sum
                        if j == 0:
                            col1 += grid[r + i][c + j]
                        elif j == 1:
                            col2 += grid[r + i][c + j]
                        elif j == 2:
                            col3 += grid[r + i][c + j]
                        
                        # for row sum
                        if i == 0:
                            row1 += grid[r + i][c + j]
                        elif i == 1:
                            row2 += grid[r + i][c + j]                       
                        elif i == 2:
                            row3 += grid[r + i][c + j]
                        
                        # for diagonal
                        if i == j:
                            diagonal1 += grid[r + i][c + j]
                        
                        if i == 2 and j == 0 or j == 2 and i == 0 or i == j == 1:
                            diagonal2 += grid[r + i][c + j]
                
                # check if magic square exist for the given 3*3 grid
                if diagonal1 == diagonal2 == row1 == row2 == row3 == col1 == col2 == col3 and len(are_unique) == 9:
                    magicSquares += 1
        
        return magicSquares