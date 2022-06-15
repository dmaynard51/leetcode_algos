class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                c[i].append((d, j))
                c[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        visit = set()
        visit.add(0)
        while heap:
            d, j = heapq.heappop(heap)
            if j not in visit:
                cnt, ans = cnt+1, ans+d
                visit.add(j)
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break        
        return ans