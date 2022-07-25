class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
            return ""
        l = 0
        r = len(palindrome)
        
        r = r // 2
        
        while l < r:
            if palindrome[l] != 'a':
                break
            l += 1
        
        if l < r:
            return palindrome[:l] + 'a' + palindrome[l+1:]
        else:
            return palindrome[:len(palindrome)-1] + 'b'