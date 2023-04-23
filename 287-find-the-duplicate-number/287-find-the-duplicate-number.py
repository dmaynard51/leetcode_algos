class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visit = set()
        
        for i in nums:
            if i in visit:
                return i
            visit.add(i)
            
        return -1