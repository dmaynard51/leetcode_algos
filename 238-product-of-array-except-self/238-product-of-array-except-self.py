class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for i in range(len(nums))]
        
        l = 0
        left = 1
        r = len(nums)-1
        right = 1

        for i in range(len(nums)):
            res[l] *= left
            left *= nums[l]
            l += 1
            res[r] *= right
            right *= nums[r]
            r -= 1
        return res
            
            
