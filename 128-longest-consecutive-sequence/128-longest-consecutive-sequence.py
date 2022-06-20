class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = set(nums)
        res = 0
        for i in nums:
            if (i - 1) not in temp:
                length = 0
                while (i + length) in temp:
                    length += 1
                res = max(res, length)
                
        return res
            