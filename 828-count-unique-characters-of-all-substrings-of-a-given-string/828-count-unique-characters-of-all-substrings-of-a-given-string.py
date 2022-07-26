class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        adj = [[-1,-1] for i in range((26))]
        dp = [0 for i in range(len(s)+1)]
        
        for i, c in enumerate(s):
            code = ord(c) - ord('A')
            first, second = adj[code]
            dp[i+1] = dp[i] + 1 + (i - 1 - second) - (second - first)
            adj[code] = [second, i]
        return sum(dp)