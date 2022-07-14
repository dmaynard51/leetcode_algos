class StockPrice(object):

    def __init__(self):
        self.min = []
        self.max = []
        self.dct = {}
        self.mTime = 0
    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.dct[timestamp] = price

        self.mTime = max(timestamp, self.mTime)
        
        heapq.heappush(self.min, [price, timestamp])
        heapq.heappush(self.max, [-price, timestamp])

    def current(self):
        """
        :rtype: int
        """
        return self.dct[self.mTime]

    def maximum(self):
        """
        :rtype: int
        """
        price, timestamp = heapq.heappop(self.max)
        
        while -price != self.dct[timestamp]:
            price, timestamp = heapq.heappop(self.max)
        
        heapq.heappush(self.max, [price, timestamp])
        return -price
    def minimum(self):
        """
        :rtype: int
        """
        price, timestamp = heapq.heappop(self.min)
        
        while price != self.dct[timestamp]:
            price, timestamp = heapq.heappop(self.min)
        
        heapq.heappush(self.min, [price, timestamp])        
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()