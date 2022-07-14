class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = len)
        res = 1
        dp = {}
        #print words
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                
                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    res = max(res, dp[word])
        return res