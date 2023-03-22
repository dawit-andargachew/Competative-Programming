class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        def getColumn(col):
            column = [ row[col] for row in matrix]
            return column

        transpose = []
        for col in range( len( matrix[0] )):
            transpose.append( getColumn(col))
        
        return transpose