class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = {i:[] for i in range(numCourses)} 
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        cycle = set()
        visit = set()
        res = []
        print adj
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visit.add(node)
            cycle.remove(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
                
            