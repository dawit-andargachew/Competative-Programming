class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]
        
        previous = self.getRow(rowIndex - 1)
        pascal = [1]*(rowIndex + 1)

        for i in range(1, rowIndex):
            pascal[i] = previous[i-1] + previous[i]

        return pascal