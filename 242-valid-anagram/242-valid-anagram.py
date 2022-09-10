class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = collections.Counter(s)
        tt = collections.Counter(t)
        res = len(tt)
        for i in range(len(s)):
            if not tt[s[i]] or tt[s[i]] <= 0:
                return False
            tt[s[i]] -= 1
            if tt[s[i]] == 0:
                res -= 1
        #print res
        return res == 0
