class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        adj = {i:[] for i in range(len(points))}
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist, i])
        visit = set()
        res = 0
                              
        q = [[0,0]]
        
        while q:
            cost, src = heapq.heappop(q)
            if src in visit:
                continue
            res += cost
            visit.add(src)
            
            for cost2, src2 in adj[src]:
                if src2 in visit:
                    continue
                heapq.heappush(q, [cost2, src2])
        return res
            
                             
                              
                              
                    