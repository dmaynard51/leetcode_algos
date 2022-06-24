class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        candidates.sort()
        #print candidates
        def dfs(idx, arr, sm, path):
            if sm == target:
                res.append(path)
                return
            if idx >= len(candidates) or sm > target:
                return
            #print path
            for i in range(idx, len(arr)):
                if i > idx and arr[i] == arr[i-1]:
                    continue
                #print path
                dfs(i+1, arr, sm + arr[i], path + [arr[i]])
        dfs(0, candidates, 0, [])
        return res
                
                