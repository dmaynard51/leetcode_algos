class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        oranges = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    oranges += 1
        
        while q and oranges > 0:
            lenQ = len(q)
            #print q
            for i in range(lenQ):
                x, y = q.popleft()
                for x1, y1 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if x1 < 0 or x1 >= len(grid) or y1 < 0 or y1 >= len(grid[0]) or grid[x1][y1] != 1:
                        continue
                    q.append([x1,y1])
                    grid[x1][y1] = 2
                    oranges -= 1
                
            count += 1
        if oranges:
            return -1
        return count
                