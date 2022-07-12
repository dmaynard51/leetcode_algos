class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        
        maxNum, minNum = 1, 1
        
        for i in nums:
            if i == 0:
                maxNum, minNum = 1, 1
                continue
            temp = i * maxNum
            maxNum = max(i * maxNum, i * minNum, i)
            minNum = min(temp, i * minNum, i)
            res = max(res, maxNum)
        return res