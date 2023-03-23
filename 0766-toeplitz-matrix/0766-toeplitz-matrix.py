class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        # check diagonal starting from each column
        for i in range( len(matrix) ):
            
            row, col = i, 0
            while row < len(matrix) - 1 and col < len( matrix[0]) - 1:
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
                
                row, col = row + 1, col + 1

        # check diagonal starting from each row
        for i in range( len(matrix[0])):

            row, col = 0, i
            while row < len(matrix) - 1  and  col < len(matrix[0]) - 1:
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
        
                row, col = row + 1, col + 1

        return True