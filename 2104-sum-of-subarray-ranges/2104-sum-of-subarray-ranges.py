class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            mn= mx = nums[i]
            for j in range(i, len(nums)):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                res += (mx - mn)
        return res