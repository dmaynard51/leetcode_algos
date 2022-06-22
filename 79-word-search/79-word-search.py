class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visit = set()
        self.res = False
        dirs = [[0,1], [0,-1], [1,0], [-1, 0]]
        def dfs(i, j, cur):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[cur] or (i,j) in visit:
                return False
            if cur+1 == len(word) and board[i][j] == word[cur]:
                return True
            
            
            visit.add((i,j))
            res = dfs(i+1,j, cur + 1) or dfs(i-1, j, cur + 1) or dfs(i, j+1, cur + 1) or dfs(i, j-1, cur + 1)
            
            if res:
                return True
            visit.remove((i,j))
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j, 0):
                    return True
        return False