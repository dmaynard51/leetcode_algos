class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        m = len(points[0])
        
        for i in range(n-1):
            for j in range(m-2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j+1] - 1)
            for j in range(m):
                points[i][j] = max(points[i][j], points[i][j-1] - 1 if j else 0)
                points[i+1][j] += points[i][j]
                
        return max(points[-1])
            