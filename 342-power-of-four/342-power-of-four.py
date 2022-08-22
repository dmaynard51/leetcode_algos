class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = float(n)
        while n > 1:
            n /= 4
        
        return n == 1