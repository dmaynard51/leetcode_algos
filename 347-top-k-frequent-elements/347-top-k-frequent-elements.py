class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dct = collections.Counter(nums)
        res = []
        lst = [[] for i in range(len(nums)+1)]
        
        for key, num in dct.items():
            lst[num].append(key)
        #print lst
        
        for i in range(len(lst)-1, -1, -1):
            res += lst[i]
            if len(res) == k:
                return res