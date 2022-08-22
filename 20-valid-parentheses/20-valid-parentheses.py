class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        fullSet = set(( '[]', '()', '{}' ))
        openParen = set(('[', '{', '('))
        stack = []
        for p in s:
            if p in openParen:
                stack.append(p)
            else:
                if not len(stack):
                    return False
                op = stack.pop()
                
                if (op + p) in fullSet:
                    continue
                else:
                    return False
        return len(stack) == 0