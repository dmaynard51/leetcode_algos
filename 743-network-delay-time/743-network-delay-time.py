class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = defaultdict(list)
        visit = set()
        
        res = 0
        
        for u, v, w in times:
            adj[u].append([w, v])
        
        q = [[0, k]]
        
        while q:
            w1, v1 = heapq.heappop(q)
            

            
            if v1 in visit:
                continue
            visit.add(v1)
            res = max(res, w1)
            
            for w2, v2 in adj[v1]:
                if v2 in visit:
                    continue
                heapq.heappush(q, [w2+ w1, v2])
            
        if len(visit) == n:
            return res
        return -1