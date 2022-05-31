class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dct = collections.Counter()
        
        l = 0
        mx = 0
        res = 0
        for r in range(len(s)):
            dct[s[r]] += 1
            mx = max(mx, dct[s[r]])
            
            if r - l - mx + 1 > k:
                dct[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res