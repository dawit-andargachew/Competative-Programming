class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        def dfs(row, col):
            # it is our of range so return Flase
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return False
            # the boarder element is X, so return True
            if (row, col) in visited or board[row][col] =="X":
                return True
            
            visited.add((row,col))

            # finally return the aggregate of the four directions
            return dfs(row + 1, col) and dfs(row - 1, col) and dfs(row, col + 1) and dfs(row, col -1)

        for i in range( len(board) ):
            for j in range( len(board[0])):
                if board[i][j] == 'O':
                    if dfs(i,j): # make a dfs and check its result

                        for v in visited:
                            board[v[0]][v[1]] = "X"

                    visited.clear()