class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = [1 for i in range(len(nums))]
        
        l, r = 0, len(nums)-1
        leftSide, rightSide = 1, 1
        for i in range(len(nums)):
            lst[l] *= leftSide
            lst[r] *= rightSide
            leftSide *= nums[l]
            rightSide *= nums[r]
            l += 1
            r -=1
        return lst
    
        #1 1 1 1
        #24 