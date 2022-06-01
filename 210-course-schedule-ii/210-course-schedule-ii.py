class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        adj = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        cycle = set()
        visit = set()
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            res.append(node)
            visit.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            