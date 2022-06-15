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
        visit.add(0)
        res = 0
        q = adj[0]                      
        heapq.heapify(q)
        
        cnt = 1
        while q:
            cost, src = heapq.heappop(q)
            if src not in visit:
                res += cost
                visit.add(src)

                for cost2, src2 in adj[src]:
                    if src2 not in visit:
                        heapq.heappush(q, [cost2, src2])
            if cnt >= len(points):
                break
        return res
            
                             
                              
                              
                    