class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        buy, sell = float('inf'), -float('inf')
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            sell = max(sell, prices[i]- buy)
        return sell