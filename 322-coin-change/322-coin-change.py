class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        #0 1  2  3  4  5
        #0 1  1  2  3  1
        for i in range(len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i-c] + 1, dp[i])
        if dp[-1] != float('inf'):
            return dp[-1]
        return -1