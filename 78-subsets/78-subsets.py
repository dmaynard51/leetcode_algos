class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        
        def dfs(i, cur):
            if i >= len(nums):
                self.res.append(cur[:])
                return
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)
        dfs(0, [])
        return self.res