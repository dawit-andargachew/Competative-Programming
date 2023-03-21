class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        # return a specific column from a given list of list
        def getColumn(col):
            st = [row[col] for row in strs ]
            return st

        # extract each column and check weather they need sorting or not
        counter = 0
        for i in range( len(strs[0]) ):

            column = getColumn(i)
            # if the column is out of order increase counter
            if column != sorted(column):
                counter += 1

        return counter