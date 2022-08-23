class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = set(nums)
        mn = float('inf')
        for i in range(1, len(nums)+1):
            if i not in temp:
                return i
        return i + 1