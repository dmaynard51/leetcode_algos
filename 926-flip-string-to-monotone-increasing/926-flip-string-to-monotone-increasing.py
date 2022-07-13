class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cnt0 = s.count('0')
        cnt1 = 0
        res = n - cnt0
        for i in s:
            if i == '0':
                cnt0 -= 1
            elif i == '1':
                res = min(res, cnt0 + cnt1)
                cnt1 +=1
        return res