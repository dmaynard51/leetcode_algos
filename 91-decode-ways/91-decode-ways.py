class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        
        #dp = [0, 1, 2]
        #01234
        #11106
        #112221
        
        for i in range(2,len(dp)):
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]