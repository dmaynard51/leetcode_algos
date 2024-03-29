class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return ''
        dct = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'],
              '5': ['j','k', 'l'], '6': ['m', 'n', 'o'], '7': ['p','q','r', 's'],
              '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        res = []
        def dfs(i, path):
            if i >= len(digits):
                res.append(path)
                return
            
            for c in dct[digits[i]]:
                dfs(i+1, path + c)
        
        dfs(0, "")
        return res