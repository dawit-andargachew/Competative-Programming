class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # validate rows and columns
        for b in board: # validate row
            row = [ r for r in b if r.isdigit()]
            if len(row) != len(set(row)):
                return False

        for j in range(9): # validate column
            col = [row[j] for row in board if row[j].isdigit()]
            if len(col) != len(set(col)):
                return False
        
        # validate each 3x3 matrixes
        r = 0
        while r < 9:
            one, two , three = [], [], []
            i = 0
            while i < 3:
                one += [c for c in board[r + i][0:3] if c.isdigit()]
                two += [c for c in board[r + i][3:6] if c.isdigit()]
                three += [c for c in board[r + i][6:9] if c.isdigit()]
                i += 1
            if len(one) != len(set(one)) or len(two) != len(set(two)) or len(three) != len(set(three)):
                return False
            r += 3

        return True 