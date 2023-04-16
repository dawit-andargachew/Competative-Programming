class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        # the question is to simulate minsweeper game and need to answer to questions
        # 1, when to stop
        #   if the given cell has adjacent mines, stop exploring and backtrack to the previos cell

        # 2, when to keep exploring
        #   if the given cell is revealed blank square, marke it as "B" and keep exploring

        # edge case, if click position is Mine, return the board by changing 'M' to 'X'
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        # all posible directions
        directions = [ [1,0],[-1,0],[0,1],[0,-1],[-1, 1],[1, -1], [1,1], [-1,-1] ]
        
        #helper function to count number of mines
        def adjacentMines(row, col):
            NumberOfMines = 0
            for d in directions:
                newrow, newcol = row + d[0], col + d[1]
                if not (newrow >= len(board) or newrow < 0 or newcol >= len(board[0]) or newcol < 0):
                    if board[newrow][newcol] == 'M':
                        NumberOfMines += 1
            
            return NumberOfMines

        def dfs(row, col, visited):
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return
                       
            if board[row][col] == 'M':
                return
            
            # store visited blockes to prevent revisiting again            
            visited.add((row, col))
            
            # call the helper function, and get the number of mines adjacent to it
            adjacent = adjacentMines(row, col) 

            # if there is adjacent mine to the given cell, assign the number of mines to it and stop exploring on its side
            if adjacent > 0:
                board[row][col] = str(adjacent)
                return
            else:
                # if there is no mine, just assign "B" and continue exploring 
                board[row][col] = 'B' 

            for d in directions:
                newrow, newcol = row + d[0], col + d[1]
                if (newrow, newcol) not in visited:
                   dfs(newrow, newcol, visited)
        
        
        # start dfs from the click position
        dfs(click[0], click[1], set())
        return board