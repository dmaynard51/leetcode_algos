class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        for x, y in points:
            heapq.heappush(res, [x*x + y*y, x, y])
        
        res2 = []
        for i in range(k):
            sm, x, y = heapq.heappop(res)
            res2.append([x,y])
        return res2