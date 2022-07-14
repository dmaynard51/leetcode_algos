class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res = []
        
        for t in tokens:
            if t not in '+-*/':
                res.append(int(t))
            else:
                n1, n2 = res.pop(), res.pop()
                if t == '+':
                    res.append(n1 + n2)
                elif t == '-':
                    res.append(n2 - n1)
                elif t == '*':
                    res.append(n1 * n2)
                else:
                    res.append(int( float(n2) / n1))
        #print res
        return res.pop()