class Solution:
    def totalNQueens(self, n: int) -> int:
        # Thsi question is a follow up question for N-QUEENS - I
        col = set()
        posDiag = set()
        negDiag = set()

        # game board with n*n size
        board = [ ["."]*n for i in range(n)]
        answer = 0

        def backtrack(r):
            nonlocal answer
            
            # when r == n, there are n Queens and each Queens don't attack another
            if r == n:
                answer += 1
                return

            # and put Queen for each row in separate columns. 
            # to prevent Queens from attaking each other
            # store diagonal cells
            for c in range(n):
                if c in col or (r + c) in posDiag or ( r - c) in negDiag:
                    continue
                
                # pick the current row and column
                col.add(c)
                posDiag.add( r + c)
                negDiag.add( r - c)
                board[r][c] = "Q"

                backtrack( r + 1)

                # don't pick the current column instead, check other columns on the current row
                col.remove(c)
                posDiag.remove( r + c)
                negDiag.remove( r - c)
                board[r][c] = "."

        backtrack(0)

        return answer