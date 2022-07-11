class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        
        minNum, maxNum = 1, 1
        
        for n in nums:
            if n == 0:
                minNum, maxNum = 1, 1
                continue
            temp = maxNum * n
            
            maxNum = max(maxNum * n, minNum * n, n)
            minNum = min(temp, minNum * n, n)
            res = max(maxNum, res)
        return res