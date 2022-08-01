class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = [0 for i in range(len(nums))]
        neg = [0 for i in range(len(nums))]
        
        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = pos[i-1] + 1 if pos[i-1] else 1
                neg[i] = neg[i-1] + 1 if neg[i-1] else 0
            elif nums[i] < 0:
                pos[i] = neg[i-1] + 1 if neg[i-1] else 0
                neg[i] = pos[i-1] + 1 if pos[i-1] else 1
        
        return max(pos)