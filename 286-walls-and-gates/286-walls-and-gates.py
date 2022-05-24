class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        rms = 0
        rows = len(rooms)
        columns = len(rooms[0])
        visit = set()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append([i, j, 0])
                    visit.add((i, j))
                elif rooms[i][j] == float('inf'):
                    r += 1

        while q:
            lenQ = len(q)
            for i in range(lenQ):
                #print q
                r, c, steps = q.popleft()
                
                for r1, c1 in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= columns or rooms[r1][c1] == -1 or (r1, c1) in visit:
                        continue
                    q.append([r1, c1, steps + 1])
                    rooms[r1][c1] = min(rooms[r1][c1], steps + 1)
                    visit.add((r1, c1))
                
                
                    
        
                    