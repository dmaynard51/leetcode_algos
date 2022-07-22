class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type s: str
        :rtype: int
        """
        res=[0]*(len(S)+1)
        idxs=[[-1,-1]]*26
        for i,c in enumerate(S):
            code=ord(c)-ord('A')
            first,second=idxs[code]
            res[i+1]=1+res[i]+(i-1-second)-(second-first)
            idxs[code]=[second,i]
        return sum(res)%(10**9+7)