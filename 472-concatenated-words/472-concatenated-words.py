class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        #dp = [0 for i in range(len(words))]
        
        def check(word, wordDict):
            if not wordDict:
                return 0
            dp = [0 for i in range(len(word)+1)]
            dp[0] = 1
            for i in range(len(dp)):
                for j in range(i):
                    if dp[j] and word[j:i] in wordDict:
                        dp[i] = max(dp[i], dp[j] + 1)
            return dp[-1]
        

        pre = set()
        words.sort(key = len)
        res = []
        for word in words:
            if check(word, pre):
                res.append(word)
            pre.add(word)
        return res