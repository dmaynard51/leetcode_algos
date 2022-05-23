class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pac = set()
        atl = set()
        rows = len(heights)
        columns = len(heights[0])
        
        def dfs(r, c, st, prev):
            if r < 0 or r >= rows or c < 0 or c >= columns or heights[r][c] < prev or (r,c) in st:
                return
            st.add((r,c))
            dfs(r+1, c, st, heights[r][c])
            dfs(r-1, c, st, heights[r][c])
            dfs(r, c+1, st, heights[r][c])
            dfs(r, c-1, st, heights[r][c])
        
        for c in range(columns):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, columns-1, atl, heights[r][columns-1])
        res = []
        
        
        for i in range(rows):
            for j in range(columns):
                if (i,j) in atl and (i, j) in pac:
                    res.append([i,j])
        return res
        