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
        q = [[0, k]]
        res = 0
        while q:
            w1, src1 = heapq.heappop(q)
            if src1 in visit:
                continue
            visit.add(src1)
            res = max(w1, res)
            
            for w2, src2 in adj[src1]:
                if src2 in visit:
                    continue
                heapq.heappush(q, [w2 + w1, src2])
        
        if len(visit) == n:
            return res
        return -1
            