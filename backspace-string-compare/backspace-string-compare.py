class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        
        def check(string):
            lst = []
            for i in string:
                if i == '#' and lst:
                    lst.pop()
                elif i != '#':
                    lst.append(i)
            return lst
        
        ss = check(s)
        tt = check(t)
        print ss, tt
        return ss == tt