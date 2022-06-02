class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        visit = set()
        
        q = deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append([i,j, 0])
        
        
        while q:
            lenQ = len(q)
            
            for i in range(lenQ):
                i, j, steps = q.popleft()
                for r1, c1 in ((i+1, j), (i-1, j), (i,j+1),(i, j-1)):
                    if r1 < 0 or r1 >= len(rooms) or c1 < 0 or c1 >= len(rooms[0]) or rooms[r1][c1] == -1 or (r1,c1) in visit:
                        continue
                    
                    q.append([r1,c1, steps+1])
                    visit.add((r1,c1))
                    rooms[r1][c1] = min(rooms[r1][c1], steps + 1)

                
                
            