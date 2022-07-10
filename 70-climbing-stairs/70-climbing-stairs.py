class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step1, step2 = 1,2
        
        #1, 2, 3,
        #s1=2 s2=3  | s1=3 s2 =5 | s1=5 s2=8 
        if n <= 2:
            return n
        for i in range(2, n):
            temp = step1 + step2
            step1 = step2
            step2 = temp
        return step2