class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        if str1 == str2:
            return str1
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif not str1.startswith(str2):
            return ''
        else:
            return self.gcdOfStrings(str1[len(str2):], str2)
        