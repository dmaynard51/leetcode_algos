class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dct = {}
        for i in range(len(nums)):
            if target - nums[i] in dct:
                return [i, dct[target - nums[i]]]
            dct[nums[i]] = i
        