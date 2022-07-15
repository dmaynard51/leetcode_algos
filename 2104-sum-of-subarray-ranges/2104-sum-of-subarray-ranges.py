class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            l, h = nums[i], nums[i]
            for j in range(i, len(nums)):
                l = min(l, nums[j])
                h = max(h, nums[j])
                res += (h-l)
        return res