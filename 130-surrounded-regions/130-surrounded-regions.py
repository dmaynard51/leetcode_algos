class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= columns or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r +1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for i in range(rows):
            for j in range(columns):
                if (board[i][j] == 'O' and (i in [0, rows-1] or j in [0, columns-1])):
                    dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T': 
                    board[i][j] = 'O'