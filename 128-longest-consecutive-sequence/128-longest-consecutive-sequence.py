class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = set(nums)
        res = 0
        for i in nums:
            if (i - 1) not in temp:
                count = 0
                
                while (i + count) in temp:
                    
                    count += 1
                res = max(res, count)
            
        return res