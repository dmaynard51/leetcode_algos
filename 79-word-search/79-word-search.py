class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visit = set()
        
        def dfs(i, j, idx):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visit or  word[idx] != board[i][j] or idx >= len(word):
                return False
            if idx ==  len(word)-1 and board[i][j] == word[idx]:
                return True
            visit.add((i, j))
            res = dfs(i+1, j, idx + 1) or dfs(i-1, j, idx + 1) or dfs(i, j+1, idx + 1) or dfs(i, j-1, idx + 1)
            
            if res:
                return True
            visit.remove((i, j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False