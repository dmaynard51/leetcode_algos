class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        #r = len(s)-1
        res = 0
        contains = set()
        for r in range(len(s)):
            while s[r] in contains and l < len(s):
                contains.remove(s[l])
                l += 1
            contains.add(s[r])
            res = max(res, r - l + 1)
        return res