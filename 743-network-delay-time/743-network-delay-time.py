class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        visit = set()
        
        q = [[0, k]]
        res = 0
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append([w, v])
        
        while q:
            c1, dst1 = heapq.heappop(q)
            if dst1 in visit:
                continue
            visit.add(dst1)
            res = max(res, c1)
            
            for c2, dst2 in adj[dst1]:
                if dst2 in visit:
                    continue
                heapq.heappush(q, [res + c2, dst2])
        
        if len(visit) == n:
            return res
        return -1