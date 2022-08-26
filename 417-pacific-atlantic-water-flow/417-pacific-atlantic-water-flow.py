class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pac = set()
        atl = set()
        
        rows = len(heights)
        cols = len(heights[0])
        
        def dfs(i, j, visit, prev):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visit or heights[i][j] < prev:
                return
            visit.add((i,j))
            dfs(i+1, j, visit, heights[i][j])
            dfs(i-1, j, visit, heights[i][j])
            dfs(i, j+1, visit, heights[i][j])
            dfs(i, j-1, visit, heights[i][j])
        
        for j in range(rows):
            dfs(j, 0, pac, 0)
            dfs(j, cols-1, atl, 0)
        
        for i in range(cols):
            dfs(0, i, pac, 0)
            dfs(rows-1, i, atl, 0)
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])
        return res