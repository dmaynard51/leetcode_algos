class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

        buy = float('inf')
        sell = -float('inf')
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            sell = max(sell, prices[i]-buy)
            #res = max(res,maxPrices- minPrices)
        return sell