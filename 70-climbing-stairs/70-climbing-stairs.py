class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        j1 = 1
        j2 = 2
        
        if n <= 2:
            return n
        # 1, 2, 3, 4, 5, 6
        # 1, 2, 3, 5, 8, 13
        
        for i in range(2, n):
            temp = (j1 + j2)
            j1 = j2
            j2 = temp
        return j2