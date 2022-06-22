class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        def dfs(i, path):
            if i == len(nums):
                self.res.append(path[:])
                return
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, path)
            
            
            
        dfs(0, [])
        return self.res