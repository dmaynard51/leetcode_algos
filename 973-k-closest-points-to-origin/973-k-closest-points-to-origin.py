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
        res.sort(key = lambda x: x[0])
        res2 = []
        for i in range(k):
            res2.append([res[i][1], res[i][2]])
        return res2