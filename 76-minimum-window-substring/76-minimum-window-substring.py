class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dct = collections.Counter(t)
        mx = float('inf')
        res = ''
        l = 0
        counter = 0
        for r in range(len(s)):
            if s[r] in dct:
                dct[s[r]] -= 1
                if dct[s[r]] == 0:
                    counter += 1

            while counter == len(dct):
                if r - l + 1 < mx:
                    res = s[l:r+1]
                    mx = r - l + 1
                if s[l] in dct:
                    if dct[s[l]] == 0:
                        counter -=1
                    dct[s[l]] += 1
                l+=1
        return res
                
                    