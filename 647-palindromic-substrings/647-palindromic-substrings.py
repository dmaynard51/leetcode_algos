class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(l, r, word):
            count = 0
            while l >= 0 and r < len(word) and word[l] == word[r]:
                l-=1
                r += 1
                count += 1
            return count
        res = 0
        for i in range(len(s)):
            res += check(i, i, s)
            res += check(i, i+1, s)
        return res