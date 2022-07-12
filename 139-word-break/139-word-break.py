class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [0 for i in range(len(s)+1)]
        
        dp[0] = 1
        #leetcode
        #1000
        #012345678
        #1000  
        for i in range(1, len(dp)):
            for w in wordDict:
                n = len(w)
                #print s[i-n:i]
                if i >= n  and w == s[i - n:i] and dp[i-n]:
                    
                    dp[i] = max(dp[i], dp[i-n] + 1)
        #print dp
        return dp[-1]
                    
                
        