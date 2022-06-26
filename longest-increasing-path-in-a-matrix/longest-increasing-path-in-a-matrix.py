class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[-1] * len(matrix[0]) for i in range(len(matrix))]
        
        def dfs(i, j, prev):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            curr = matrix[i][j]
            
            dp[i][j] = 1 + max(dfs(i+1, j, curr), dfs(i-1,j, curr), dfs(i, j+1, curr), dfs(i, j-1, curr))
            return dp[i][j]
        
        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i,j,-1))
        return res