class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visit = set()
        res = 0
        def dfs(i, j, grid):
            if (i,j) in visit or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return 0
            visit.add((i,j))
            dfs(i+1, j, grid)
            dfs(i-1, j, grid)
            dfs(i, j+1, grid)
            dfs(i, j-1, grid)
            return 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += dfs(i,j, grid)
        return res