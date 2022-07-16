class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def check(w, wordDict):
            if not wordDict:
                return False
            
            dp = [0 for i in range(len(w) + 1)]
            dp[0] = 1
            
            for i in range(len(dp)):
                for j in range(i):
                    if dp[j] and w[j:i] in wordDict:
                        dp[i] = max(dp[i], dp[j]+1)
                        break
            #print dp
            return dp[-1]
        
        words.sort(key = len)
        pre = set()
        res = []
        #print words
        for w in words:
            if check(w, pre):
                res.append(w)
            pre.add(w)
        return res