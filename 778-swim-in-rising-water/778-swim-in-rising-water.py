class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set((0, 0))
        q = [[grid[0][0], 0, 0]]
        
        
        
        while q:
            cost1, i, j = heapq.heappop(q)
            if i == len(grid)-1 and j == len(grid[0])-1:
                return cost1
            
            for i2, j2 in dirs:
                i2, j2 = i2 + i, j2 + j
                
                if i2 < 0 or i2 >= len(grid) or j2 < 0 or j2 >= len(grid[0]) or (i2, j2) in visit:
                    continue
                visit.add((i2, j2))
                heapq.heappush(q, [max(cost1, grid[i2][j2]), i2, j2])