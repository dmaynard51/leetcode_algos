class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[0])):
                    grid[i][j] = 1-grid[i][j]
        
        for j in range(len(grid[0])):
            z = 0
            o = 0
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    o += 1
                else:
                    z += 1
            
            if z > o:
                for i in range(len(grid)):
                    grid[i][j] = 1 - grid[i][j]
        
        for i in range(len(grid)):
            s = ''
            for j in range(len(grid[0])):
                s += str(grid[i][j])
            res += int(s, 2)
        return res
                