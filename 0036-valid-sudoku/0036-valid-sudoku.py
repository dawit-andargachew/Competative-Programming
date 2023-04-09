class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

       # validate rows and columns
        for row in board: # validate row
            a = [ r for r in row if r.isdigit()]
            if len(a) != len(set(a)):
                return False
        
        for j in range( len(board)): # validate column
            col = [row[j] for row in board if row[j].isdigit()]

            if len(col) != len(set(col)):
                return False

        # validate each 3x3 matrixes
        r = 0
        while r < len(board):
            one, two, three = [], [], []

            # one = [ for c in board[r]]
            
            # first 3 * 3
            j, i = 0, 0
            while i < 3:
                while j < 3:
                    if board[r + i][j].isdigit():
                        one.append(board[r + i][j])
                    j += 1
                i, j = i + 1, 0
            if len(one) != len(set(one)):
                return False

            # second 3 * 3
            j, i = 3, 0
            while i < 3:
                while j < 6:
                    if board[r + i][j].isdigit():
                        two.append(board[r + i][j])
                    j += 1
                i, j = i + 1, 3
            if len(two) != len(set(two)):
                return False
            
            # third 3 * 3
            j, i = 6, 0
            while i < 3:
                while j < 9:
                    if board[r + i][j].isdigit():
                        three.append(board[r + i][j])
                    j += 1
                i, j = i + 1, 6
            if len(three) != len(set(three)):
                return False

            r += 3

        return True
    