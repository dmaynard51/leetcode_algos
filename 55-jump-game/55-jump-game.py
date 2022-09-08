class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxJump = nums[0]
        curJump = nums[0]
        for i in range(1,len(nums)):
            curJump -= 1
            if curJump < 0:
                return False
            curJump = max(nums[i], curJump)
        return True