class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visit = set()
        res = 0
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i,j) in visit or grid[i][j] != '1':
                return 0
            visit.add((i,j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += dfs(i,j)
        return res