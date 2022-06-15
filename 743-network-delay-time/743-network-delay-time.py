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
        q = [[0, k]]
        
        visit = set()
        res = 0
        while q:
            w1, dst1 = heapq.heappop(q)
            
            if dst1 in visit:
                continue
            visit.add(dst1)
            res = max(w1, res)
            for w2, dst2 in adj[dst1]:
                if dst2 in visit:
                    continue
                heapq.heappush(q, [w2 + w1, dst2])
        if len(visit) == n:
            return res
        return -1