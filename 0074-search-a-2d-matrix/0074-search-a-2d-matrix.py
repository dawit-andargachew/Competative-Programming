class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = len(matrix), len(matrix[0])
        
        #search over first column and specify the row
        if matrix[0][0] > target or matrix[ row - 1 ][col - 1] < target:
            return False
        
        # find the specific row the number is expected to present
        target_row = -1
        for i in range(row):
            if matrix[i][col - 1] >= target:
                target_row = i
                break
        
        # check if the target_row is the last row
        if target_row == -1:
            target_row = row - 1

        # iterate over the target_row and find the element
        for i in range (col):
            if matrix[target_row][i] == target:
                return True
        
        # the element is not in the matrix so return False
        return False