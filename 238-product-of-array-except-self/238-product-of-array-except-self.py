class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for i in range(len(nums))]
        l, r = 0, len(nums)-1
        left, right = 1, 1
        while l < len(nums):
            res[l] *= left
            res[r] *= right
            left *= nums[l]
            right *= nums[r]
            l += 1
            r -=1
        
        return res
    
        
        #[1,2,3,4]
        #[1,1,1,1]
        #1,1,2,6
        #24,12,4,1
        #24,12,8,6