class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dct = collections.Counter(nums)
        
        res = [[] for i in range(len(nums)+1)]

        res2 = []
        for n, c in dct.items():
            res[c].append(n)

        for i in range(len(res)-1, -1, -1):
            bucket = res[i]
            res2 += bucket
            if len(res2) == k:
                return res2
        
        
        