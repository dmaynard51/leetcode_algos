class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        cur = []
        def rec(left, right):
            if left == right == n:
                res.append(''.join(cur))
                return
            if left < n:
                cur.append('(')
                rec(left+1, right)
                cur.pop()
            
            if right < left:
                cur.append(')')
                rec(left, right +1)
                cur.pop()
        
        rec(0,0)
        return res