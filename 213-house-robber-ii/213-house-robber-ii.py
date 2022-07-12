class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def check(arr):
            rob1, rob2 = 0, 0
            
            for i in arr:
                temp = max(rob2, rob1 + i)
                rob1 = rob2
                rob2 = temp
            return rob2
        if len(nums) <=1 :
            return nums[-1]
        return max(check(nums[1:]), check(nums[:-1]) )
        