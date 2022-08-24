class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = float(n)
        while n > 1:
            n /= 3

        return n == 1
        