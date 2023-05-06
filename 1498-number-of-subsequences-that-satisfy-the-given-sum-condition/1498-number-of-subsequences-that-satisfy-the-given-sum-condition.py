class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        count = 0

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += pow(2, right - left, MOD)
                left += 1

        return count % MOD