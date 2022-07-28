class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        ss = collections.Counter(s)
        tt = collections.Counter(t)
        
        for key, val in ss.items():
            if tt[key] != val:
                return False
        return True
        