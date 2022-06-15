class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = defaultdict(list)
        
        for u, v, w in times:
            adj[u].append([w, v])
        
        visit = set()
        res = 0
        
        q = [[0, k]]
        res = 0
        while q:
            w1, v1 = heapq.heappop(q)
            if len(visit) == n:
                return res
            
            if v1 in visit:
                continue
            res = max(res, w1)
            visit.add(v1)
            for w2, v2 in adj[v1]:
                if v2 in visit:
                    continue
                heapq.heappush(q, [w2+w1, v2])
        if len(visit) == n:
            return res
        return -1