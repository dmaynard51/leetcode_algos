class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax, curMin = 1, 1
        res = max(nums)
        for i in nums:
            if i == 0:
                curMax, curMin = 1, 1
                continue
            temp = i * curMax
            curMax = max(i * curMax, i * curMin, i)
            curMin = min(temp, i * curMin, i)
            res = max(res, curMax)
        return res