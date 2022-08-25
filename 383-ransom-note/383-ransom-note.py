class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        
        for i in ransomNote:
            if not m[i] or m[i] < 0:
                return False
            m[i] -= 1
        
        return True