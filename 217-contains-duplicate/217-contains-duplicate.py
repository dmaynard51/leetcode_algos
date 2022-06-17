class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visit = set()
        
        for i in nums:
            if i in visit:
                return True
            visit.add(i)
        return False