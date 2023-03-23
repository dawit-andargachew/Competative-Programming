class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # if there size is not equal return the original matrix
        if len(mat) * len( mat[0]) != r * c:
            return mat

        # append new list to the answer whenever temp lengt is equal to new column
        ans, temp = [],[]
        for row in range( len(mat) ):
            for col in range(len(mat[0])):

                if len(temp) == c:
                    ans.append( temp[:])
                    temp.clear()

                temp.append( mat[row][col] )
            
        if len(temp) == c:
            ans.append( temp[:])

        return ans