class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        
        properties.sort(key = lambda x: (-x[0], x[1]))
        res = 0
        mxD = 0
        for _, d in properties:
            if d < mxD:
                res += 1
            else:
                mxD = d
        return res