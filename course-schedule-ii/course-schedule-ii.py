class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = defaultdict(list)
        for src, nei in prerequisites:
            adj[src].append(nei)
        
        visit = set()
        
        cycle = set()
        res = []
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
            visit.add(node)
            res.append(node)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res