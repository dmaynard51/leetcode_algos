class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        #
        def dfs(i, path, sm):
            if sm == target:
                res.append(path[:])
                return
            if i >= len(candidates) or sm > target:
                return
            path.append(candidates[i])
            dfs(i, path, sm + candidates[i])
            #print path
            path.pop()
            dfs(i+1, path, sm)
            return
        
        dfs(0, [], 0)
        return res