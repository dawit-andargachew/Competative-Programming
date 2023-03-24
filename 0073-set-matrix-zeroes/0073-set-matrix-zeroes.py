class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zeros = []
        row, col = len(matrix), len(matrix[0])

        # identify the indices which are zero
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zeros.append([r,c])
        
        # set the row and column of those indices to zero
        while zeros:

            # to chnage the row to zero, row is contant and so iterate over the column
            for c in range(col):
                matrix[ zeros[-1][0] ][c] = 0
            
            # to change the column to zero,column is contant so iterate over the row
            for r in range(row):
                matrix[r][ zeros[-1][1] ] = 0
            
            # remove the last element chaning row and column to zero
            zeros.pop()