class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def check(s, wordDict):
            if not wordDict:
                return False
            
            dp = [0 for i in range(len(s)+1)]
            dp[0] = 1
            for i in range(len(dp)):
                for j in range(i):
                    if dp[j] and s[j:i] in wordDict:
                        dp[i] = max(dp[i], dp[j] + 1)
            
            return dp[-1]
        
        pre = set()
        res = []
        words.sort(key = len)
        for word in words:
            if check(word, pre):
                res.append(word)
            pre.add(word)
        return res
             