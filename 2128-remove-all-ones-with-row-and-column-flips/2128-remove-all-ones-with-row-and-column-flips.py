class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        
        m1 = grid[0]
        m2 = [1 - x for x in grid[0]]
        
        
        for i in range(1, m):
            if grid[i] != m1 and grid[i] != m2:
                return False
        return True