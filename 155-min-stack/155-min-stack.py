class MinStack(object):

    def __init__(self):
        self.min = []
        self.arr = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(val, self.min[-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()
        self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()