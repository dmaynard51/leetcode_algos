class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(n):
            rob1, rob2 = 0, 0
            
            for i in n:
                temp = max(rob1 + i, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        if len(nums) <= 2:
            return max(nums)
        
        return max(dfs(nums[1:]), dfs(nums[:-1]))