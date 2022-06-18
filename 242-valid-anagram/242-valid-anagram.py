class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = collections.Counter(s)
        tt = collections.Counter(t)
        
        return ss == tt