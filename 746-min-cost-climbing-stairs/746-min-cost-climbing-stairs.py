class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(cost)+1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        
        for i in range(2, len(cost)):
            dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])
        dp[-1] = min(dp[-2], dp[-3])
        return dp[-1]