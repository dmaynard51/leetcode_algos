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
        visit = set()
        prices = [float('inf') for i in range(n)]
        prices[src] = 0
        
        for i in range(k +1):
            temp = prices[:]
            
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            
            prices = temp
        if prices[dst] != float('inf'):
            return prices[dst]
        return -1