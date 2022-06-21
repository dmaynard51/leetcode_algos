class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(i, sm, cur):
            if sm == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or sm > target:
                return
            cur.append(candidates[i])
            dfs(i, sm + candidates[i], cur)
            cur.pop()
            dfs(i+1, sm, cur)
        dfs(0, 0, [])
        return res