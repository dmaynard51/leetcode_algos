class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        prices = [float('inf') for i in range(n)]
        prices[src] = 0
        for i in range(k+1):
            temp = prices[:]
            
            for s, d, c in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + c < temp[d]:
                    temp[d] = prices[s] + c
            prices = temp
        
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]