class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        st = set(wordDict)
        
        
        

        
        dp = [0 for i in range(len(s)+1)]
        
        
        dp[0] = 1
        for i in range(len(dp)):
            for j in range(i):
                #print s[j:i]
                if dp[j] and s[j:i] in st:
                    
                    dp[i] = max(dp[i], dp[j] + 1)
        #print dp
        return dp[-1]