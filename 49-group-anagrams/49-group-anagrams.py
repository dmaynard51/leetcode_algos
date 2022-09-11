class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct = defaultdict(list)
        
        for word in strs:
            w = ''.join(sorted(word))
            
            dct[w].append(word)
        res = []
        for lst in dct:
            res.append(dct[lst])
        return res