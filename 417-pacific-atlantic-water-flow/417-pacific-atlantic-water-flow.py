class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pac = set()
        atl = set()
        
        res = []
        rows = len(heights)
        columns = len(heights[0])
        
        def dfs(i, j, st, prev):
            if i < 0 or i >= rows or j < 0 or j >= columns or heights[i][j] < prev or (i,j) in st:
                return
            
            st.add((i,j))
            dfs(i+1, j, st, heights[i][j])
            dfs(i-1, j, st, heights[i][j])
            dfs(i, j+1, st, heights[i][j])
            dfs(i, j-1, st, heights[i][j])
            
            
        
        
        for c in range(columns):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1,c, atl, heights[rows-1][c])
            
            
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, columns-1, atl, heights[r][columns-1] )
            
        #print atl, pac
        for i in range(rows):
            for j in range(columns):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res