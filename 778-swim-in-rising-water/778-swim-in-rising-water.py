class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = [[grid[0][0], 0, 0]]
        
        visit = set()
        visit.add((0,0))
        n = len(grid)
        directions = [[1, 0], [-1, 0], [0,1], [0, -1]]
        while q:
            t, r, c = heapq.heappop(q)
            if r == n-1 and c == n-1:
                return t            
            
            for r1, c1 in directions:
                r1, c1 = r1 + r, c1 + c

                if r1 < 0 or r1 >= n or c1 < 0 or c1 >= n or (r1, c1) in visit:
                    continue
                visit.add((r1, c1))
                heapq.heappush(q, [max(t, grid[r1][c1]), r1, c1])