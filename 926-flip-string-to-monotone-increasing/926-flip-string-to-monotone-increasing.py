class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count0 = s.count('0')
        count1 = 0
        res = len(s) - count0
        
        for i in s:
            if i == '0':
                count0 -=1
            elif i == '1':
                res = min(res, count0 + count1)
                count1 += 1
        return res