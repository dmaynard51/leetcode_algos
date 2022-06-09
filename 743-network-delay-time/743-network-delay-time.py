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
        
        for src, dst, cost in times:
            adj[src].append([cost, dst])
        q = [[0, k]]
        res = 0

        while q:
            c1, src1 = heapq.heappop(q)
            if src1 in visit:
                continue
            visit.add(src1)
            res = max(res, c1)
            for c2, src2 in adj[src1]:
                if src2 in visit:
                    continue
                heapq.heappush(q, [c2 + c1, src2])
        if len(visit) == n:
            return res
        return -1
        