class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[0] == 0 and len(nums) >= 2:
            return False
        if nums[0] == 0 and len(nums)== 1:
            return True
        res = [0 for i in range(len(nums))]
        res[0] = nums[0]
        for i in range(1, len(nums)):
            #print res
            res[i] = max(nums[i], res[i-1] - 1)
            if res[i] <= 0 and i != len(nums)-1:
                return False
            elif res[i] + i >= len(nums)-1:
                return True
        return True