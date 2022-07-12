class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step1 = 1
        step2 = 2
        if n <= 2:
            return n
        for i in range(2, n):
            temp = step1 + step2
            step1 = step2
            step2 = temp
        return step2