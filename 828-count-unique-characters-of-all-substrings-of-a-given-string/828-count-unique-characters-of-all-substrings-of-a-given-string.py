class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = [[-1, -1] for i in range(26)] 
        res = [0 for i in range(len(s)+1)]
        
        for i,c in enumerate(s):
            code = ord(c) - ord('A')
            first, second = idx[code]
            res[i+1] = res[i] + 1 + (i - 1 - second) - (second - first)
            idx[code] = [second, i]
        return sum(res) % (2**32-1)