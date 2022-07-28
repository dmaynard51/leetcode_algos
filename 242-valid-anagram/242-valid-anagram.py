class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        s = sorted(''.join(s))
        t = sorted(''.join(t))
        return s == t