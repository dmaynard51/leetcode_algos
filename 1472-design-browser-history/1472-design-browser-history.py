class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.future = []
        self.history = [homepage]

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        #print self.stack
        self.history.append(url)
        self.future = []
        
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and len(self.history) > 1:
            steps -= 1
            self.future.append(self.history[-1])
            self.history.pop()
        return self.history[-1]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.future:
            steps -= 1
            self.history.append(self.future.pop())
            #self.future.pop()
        return self.history[-1]        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)