class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def dfs(l, r, word):
            while l >= 0 and r < len(s) and word[l] == word[r]:
                l -= 1
                r +=1
            return word[l+1:r]
        
        res = ""
        curMax = 0
        for i in range(len(s)):
            temp1 = dfs(i, i, s)
            temp2 = dfs(i, i+1, s)
            if len(temp1) > len(temp2):
                if len(temp1) > curMax:
                    res = temp1
                    curMax = len(temp1)
            else:
                if len(temp2) > curMax:
                    curMax = len(temp2)
                    res = temp2
        return res
                
            
                
                