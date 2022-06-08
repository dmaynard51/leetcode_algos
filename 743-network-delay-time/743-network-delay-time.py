class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #djiktras
        adj = defaultdict(list)
        
        for u, v, w in times:
            adj[u].append([w, v])
        visit= set()
        t = 0
        #print adj
        q = [[0, k]]
        #print adj
        while q:
            w1, v1 = heapq.heappop(q)
            
            if v1 in visit:
                continue
            visit.add(v1)
            t = max(t, w1)
            for w2, v2 in adj[v1]:
                if v2 in visit:
                    continue
                heapq.heappush(q, [w2 + w1, v2])
        if len(visit) == n:
            return t
        return -1