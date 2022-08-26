class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        cur = 0
        for i in range(len(nums)):
            cur = max(cur + nums[i], nums[i])
            res = max(cur, res)
        return res
            
    
                